from django import forms

class UserForm(forms.Form):


    profile = forms.CharField(label="本文",widget=forms.Textarea())
    sound_profile = forms.CharField(max_length=200,label="サウンドURL")
    user_icon = forms.CharField(max_length=200,label="アイコンURL")
    birthday = forms.DateField(label="誕生日")
    # email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user_name = models.OneToOneField(User, on_delete=models.CASCADE)