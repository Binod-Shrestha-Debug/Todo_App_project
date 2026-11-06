from django.contrib import admin
from .models import Task, Category, Tag, TaskActivity, Comment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "priority", "due_date")
    list_filter = ("status", "priority", "created_at")
    search_fields = ("title", "description", "user__username")

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(TaskActivity)
admin.site.register(Comment)
