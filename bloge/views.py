from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import PostSerializer, UserSerializer
from .models import Post
from django.contrib.auth.models import User

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer