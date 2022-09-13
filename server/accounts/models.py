from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class AccountUser(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.CharField("パスワード", max_length=200)
    profile = models.TextField("本文")
    sound_profile = models.CharField("サウンドURL", max_length=200)
    user_icon = models.CharField("アイコンURL", max_length=200)
    created = models.DateField("誕生日")
    # email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user_name = models.OneToOneField(User, on_delete=models.CASCADE)

def __str__(self):
        return self.user_name