from django.db import models
from posts.models import *
from django.contrib.auth.models import User

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='comments_comment', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user}'