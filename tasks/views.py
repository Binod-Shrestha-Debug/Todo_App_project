from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import TaskForm, CategoryForm, CommentForm
from .models import Task, Category, TaskActivity

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user).select_related("category")
    context = {
        "total_count": tasks.count(),
        "completed_count": tasks.filter(status=Task.Status.COMPLETED).count(),
        "progress_count": tasks.filter(status=Task.Status.IN_PROGRESS).count(),
        "pending_count": tasks.filter(status=Task.Status.PENDING).count(),
        "overdue_count": sum(1 for task in tasks if task.is_overdue),
        "recent_tasks": tasks.order_by("-created_at")[:6],
        "today": timezone.localdate(),
    }
    return render(request, "tasks/dashboard.html", context)


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).select_related("category").prefetch_related("tags")
    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "")
    priority = request.GET.get("priority", "")
    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)
    return render(request, "tasks/task_list.html", {
        "tasks": tasks, "query": query, "selected_status": status,
        "selected_priority": priority,
        "status_choices": Task.Status.choices,
        "priority_choices": Task.Priority.choices,
    })


@login_required
def task_create(request):
    form = TaskForm(request.POST or None, user=request.user)
    if request.method == "POST" and form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        form.save_m2m()
        TaskActivity.objects.create(task=task, user=request.user, message="Task created")
        messages.success(request, "Task created successfully.")
        return redirect("task_list")
    return render(request, "tasks/task_form.html", {"form": form, "heading": "Create task"})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    comment_form = CommentForm(request.POST or None)
    if request.method == "POST" and comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.task = task
        comment.user = request.user
        comment.save()
        TaskActivity.objects.create(task=task, user=request.user, message="Comment added")
        messages.success(request, "Comment added.")
        return redirect("task_detail", pk=pk)
    return render(request, "tasks/task_detail.html", {
        "task": task, "comment_form": comment_form
    })


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    form = TaskForm(request.POST or None, instance=task, user=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
        TaskActivity.objects.create(task=task, user=request.user, message="Task updated")
        messages.success(request, "Task updated successfully.")
        return redirect("task_detail", pk=pk)
    return render(request, "tasks/task_form.html", {"form": form, "heading": "Update task"})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted.")
        return redirect("task_list")
    return render(request, "tasks/confirm_delete.html", {"task": task})


@login_required
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.status = Task.Status.COMPLETED if task.status != Task.Status.COMPLETED else Task.Status.PENDING
        task.save()
        TaskActivity.objects.create(task=task, user=request.user, message=f"Status changed to {task.get_status_display()}")
    return redirect(request.META.get("HTTP_REFERER", "task_list"))


@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    form = CategoryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        category = form.save(commit=False)
        category.user = request.user
        category.save()
        messages.success(request, "Category added.")
        return redirect("category_list")
    return render(request, "tasks/categories.html", {"categories": categories, "form": form})


@login_required
def calendar_view(request):
    tasks = Task.objects.filter(user=request.user, due_date__isnull=False).select_related("category")
    return render(request, "tasks/calendar.html", {"tasks": tasks})
