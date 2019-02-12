from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User,related_name='owener', on_delete=models.CASCADE, null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, Created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    @classmethod
    def unfriend(cls, current_user, new_friend):
        friend, Created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)
