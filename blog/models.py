from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that the date will be added automatically when the post is created
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True means that the date will be added automatically when the post is updated
    def __str__(self):
        return self.title + ' | ' + str(self.author) # str(self.author) is used to convert the author object to a string so that it can be displayed in the admin panel
