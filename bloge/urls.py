from django.urls import path
from .views import (
    PostViewSet
)
from rest_framework.routers import SimpleRouter

urlpatterns = []

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns += router.urls