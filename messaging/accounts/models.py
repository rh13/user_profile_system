from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE,
        primary_key=True,)
	description= models.CharField(max_length=50)
	city=models.CharField(max_length=50)
	contact = models.IntegerField(default='')


	def __str__(self):
		return self.user.username
