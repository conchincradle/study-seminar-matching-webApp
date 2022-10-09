from distutils.command.upload import upload
from django import forms

from .models import AccountUser



class ProfileEditForm(forms.ModelForm):


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
        fields = ('user_name', 'profile','sound_profile','user_icon', 'birthday',)


