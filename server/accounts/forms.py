from distutils.command.upload import upload
from django import forms

from .models import AccountUser

# class ProfileEditForm(forms.Form):
#     name = forms.CharField(max_length=50, label='名前')
#     profile = forms.CharField(label='自己紹介', widget=forms.Textarea())
#     birthday = forms.DateField(label="生年月日")
#     #icon = forms.ImageField(upload_to='???')

#     def __str__(self):
#         return self.name

class ProfileEditForm(forms.ModelForm):
    # user_name = forms.CharField(max_length=50, label='名前')
    # profile = forms.CharField(label='自己紹介', widget=forms.Textarea())
    # birthday = forms.DateField(label="生年月日")
    #icon = forms.ImageField(upload_to='???')

    class Meta:
        model = AccountUser
        fields = ('user_name', 'profile', 'birthday')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

    def update(self, user):
        user.user_name = self.cleaned_data['user_name']
        user.profile = self.cleaned_data['profile']
        user.birthday = self.cleaned_data['birthday']
        user.save()

class UserForm(forms.ModelForm):
    class Meta:
        model = AccountUser
        fields = ('user_icon', 'birthday', 'profile','sound_profile')

    #profile = forms.CharField(label="本文",widget=forms.Textarea())
    #sound_profile = forms.CharField(max_length=200,label="サウンドURL")
    #user_icon = forms.CharField(max_length=200,label="アイコンURL")
    #birthday = forms.DateField(label="誕生日")
    # email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user_name = models.OneToOneField(User, on_delete=models.CASCADE)

