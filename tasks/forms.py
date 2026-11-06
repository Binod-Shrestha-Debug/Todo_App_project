from django import forms
from .models import Task, Category, Tag

class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )
    start_date = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )

    class Meta:
        model = Task
        fields = ["title", "description", "category", "tags", "priority", "status", "start_date", "due_date"]
        widgets = {"description": forms.Textarea(attrs={"rows": 4})}

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields["category"].queryset = Category.objects.filter(user=self.user)
            self.fields["tags"].queryset = Tag.objects.filter(user=self.user)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "color"]
        widgets = {"color": forms.TextInput(attrs={"type": "color"})}


class CommentForm(forms.ModelForm):
    class Meta:
        from .models import Comment
        model = Comment
        fields = ["body"]
        widgets = {"body": forms.Textarea(attrs={"rows": 3, "placeholder": "Write a comment..."})}
