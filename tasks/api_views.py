from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Count
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from .permissions import IsTaskOwner

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsTaskOwner]
    filterset_fields = ["status", "priority", "category"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "due_date", "priority", "title"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).select_related("category").prefetch_related("tags")

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def dashboard_stats(request):
    tasks = Task.objects.filter(user=request.user)
    return Response({
        "total": tasks.count(),
        "completed": tasks.filter(status=Task.Status.COMPLETED).count(),
        "in_progress": tasks.filter(status=Task.Status.IN_PROGRESS).count(),
        "pending": tasks.filter(status=Task.Status.PENDING).count(),
        "by_priority": list(tasks.values("priority").annotate(count=Count("id")).order_by("priority")),
    })
