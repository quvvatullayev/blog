from rest_framework.serializers import Serializer
from blog.models import Post
from django.contrib.auth.models import User

class UserSerializer(Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(Serializer):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'created_at', 'updated_at')
        depth = 1