from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Task

class TaskApiTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="StrongPass123!")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_can_create_task(self):
        response = self.client.post("/api/tasks/", {
            "title": "Test task",
            "priority": "high",
            "status": "pending"
        }, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Task.objects.filter(user=self.user, title="Test task").exists())

    def test_user_only_sees_own_tasks(self):
        other = User.objects.create_user(username="other", password="StrongPass123!")
        Task.objects.create(user=other, title="Private task")
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)
