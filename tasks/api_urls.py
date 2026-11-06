from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import TaskViewSet, CategoryViewSet, dashboard_stats

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="api-task")
router.register("categories", CategoryViewSet, basename="api-category")

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/", dashboard_stats, name="api-dashboard"),
]
