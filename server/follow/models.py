from pyexpat import model
import django
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import AccountUser

class FollowRelation(models.Model):
    user = models.OneToOneField(AccountUser, primary_key=True, on_delete=models.CASCADE)
    following = models.ManyToManyField(AccountUser, related_name='followed_by', blank=True)

    def __str__(self):
        return str(self.user.user_name)
