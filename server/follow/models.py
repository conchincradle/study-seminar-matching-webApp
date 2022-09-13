import django
from django.db import models
from django.conf import settings
from django.utils import timezone
from accounts.models import AccountUser

class FollowRelation(models.Model):
    following = models.ForeignKey(AccountUser, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(AccountUser, related_name='follower', on_delete=models.CASCADE)
