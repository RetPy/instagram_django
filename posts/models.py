from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag

class Post(models.Model):
    text = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_user')
    tag = models.ManyToManyField(Tag, verbose_name='tag', related_name='tags')

    def __str__(self):
        return self.id

class PostImage(models.Model):
    image = models.ImageField(upload_to = 'image',null=True, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_image',null=True, blank=True)

    def __str__(self):
        return self.post.id

class Like(models.Model):
    user_like = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post_like = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts_like')