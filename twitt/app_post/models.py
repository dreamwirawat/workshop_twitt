from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    id_tag = models.ManyToManyField('Tag', through='PostTag')

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

class Sex(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sex')
    avatar = models.IntegerField(default=0)

class Tag(models.Model):
    tag_content = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)