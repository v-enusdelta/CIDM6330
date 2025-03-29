from django.db import models # Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
 
class Post(models.Model):
 
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
 
    def __str__(self) -> str:
        return self.title

