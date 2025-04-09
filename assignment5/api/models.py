from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
    isadmin = models.BooleanField(default=False)
    isreporter = models.BooleanField(default=False)
    isanalyst = models.BooleanField(default=False)
    isviewer = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Session(models.Model):
    sessionid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    sessionkey = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.sessionkey
    
class Event(models.Model):
    eventid = models.AutoField(primary_key=True)
    sessionid = models.ForeignKey(Session, on_delete=models.CASCADE)
    itemid = models.CharField(max_length=100)
    eventtime = models.DateTimeField(auto_now_add=True)
    eventtype = models.CharField(max_length=100)

    def __str__(self):
        return self.eventid
    
