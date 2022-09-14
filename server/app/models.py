import django
from django.db import models
from django.conf import settings
from django.utils import timezone
from accounts.models import AccountUser
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")
    created = models.DateTimeField("作成日", default=timezone.now)

    def __str__(self):
        return self.title

class AppComment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    

class AppSeminar(models.Model):
    content = models.TextField("本文")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.CharField("会議URL", max_length=200)
    created = models.DateTimeField("作成日", default=timezone.now)
    title = models.CharField("タイトル", max_length=200)

    def __str__(self):
        return self.title


class AppSeminarParticipant(models.Model):
    user = models.ForeignKey(AccountUser,  on_delete=models.CASCADE)
    seminar = models.ForeignKey(AppSeminar, on_delete=models.CASCADE)