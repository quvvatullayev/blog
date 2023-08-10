from rest_framework import generics
from .serializers import PostSerializer, UserSerializer
from .models import Post
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'body', 'author']
    ordering_fields = ['title', 'body', 'author', 'created_at', 'updated_at']
    ordering = ['title', 'body', 'author', 'created_at', 'updated_at']
    search_fields = ['$title', '$body', '$author__username']
