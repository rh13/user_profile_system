from django.db import models
from django.contrib.auth.models import User

class CachedMessage(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=1024)

    def __str__(self):
        return self.writer.username

class UserMessage(models.Model):
    read = models.BooleanField(default=False)
    message = models.IntegerField()

class Inbox(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    messages = models.ManyToManyField(UserMessage)
    def __str__(self):
        return self.owner.username
