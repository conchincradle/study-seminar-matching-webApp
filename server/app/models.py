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
    content = models.TextField("コメント内容")
    created = models.DateTimeField("作成日", default=timezone.now)
    author_id = models.ForeignKey(AccountUser, on_delete=models.CASCADE)
    posted_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    

class AppSeminar(models.Model):
    content = models.TextField("本文")
    author_id = models.ForeignKey(AccountUser, related_name='author_id', on_delete=models.CASCADE)
    link = models.CharField("会議URL", max_length=200)
    created = models.DateTimeField("作成日", default=timezone.now)
    title = models.CharField("タイトル", max_length=200)

    def __str__(self):
        return self.title


class AppSeminarParticipant(models.Model):
    user_id = models.ForeignKey(AccountUser,  on_delete=models.CASCADE)
    seminar_id = models.ForeignKey(AppSeminar, on_delete=models.CASCADE)