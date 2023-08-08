from rest_framework.serializers import Serializer, ModelSerializer
from bloge.models import Post
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(ModelSerializer):
    # author = UserSerializer()
    class Meta:
        model = Post
        fields = ['id','title', 'author', 'body', 'created_at', 'updated_at']