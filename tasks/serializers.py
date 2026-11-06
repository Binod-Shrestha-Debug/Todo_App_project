from rest_framework import serializers
from .models import Task, Category, Tag, Comment, TaskActivity

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "color", "created_at"]
        read_only_fields = ["id", "created_at"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.none(), required=False)

    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "category", "category_name", "tags",
            "priority", "status", "start_date", "due_date", "created_at", "updated_at"
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            self.fields["tags"].queryset = Tag.objects.filter(user=request.user)
            self.fields["category"].queryset = Category.objects.filter(user=request.user)

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("A task title cannot be empty.")
        return value.strip()

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        task = Task.objects.create(user=self.context["request"].user, **validated_data)
        task.tags.set(tags)
        TaskActivity.objects.create(task=task, user=task.user, message="Task created through API")
        return task

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        if tags is not None:
            instance.tags.set(tags)
        TaskActivity.objects.create(task=instance, user=instance.user, message="Task updated through API")
        return instance


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "username", "body", "created_at"]
        read_only_fields = ["id", "username", "created_at"]
