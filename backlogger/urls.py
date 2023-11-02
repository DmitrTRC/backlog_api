from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BackLogItemViewSet


router = DefaultRouter()
router.register(r'backlog-items', BackLogItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
