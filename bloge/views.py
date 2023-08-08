from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import PostSerializer, UserSerializer
from .models import Post
from django.contrib.auth.models import User
from rest_framework.views import APIView

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ['title', 'body']

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
