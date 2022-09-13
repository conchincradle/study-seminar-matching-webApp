from django.db import models
from django.conf import settings
from django.utils import timezone

class AccountUser(models.Model):
    password = models.CharField("パスワード", max_length=200)
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile = models.TextField("本文")
    sound_profile = models.CharField("サウンドURL", max_length=200)
    user_icon = models.CharField("アイコンURL", max_length=200)
    created = models.DateField("誕生日")
    # email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

