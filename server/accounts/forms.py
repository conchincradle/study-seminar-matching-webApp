from distutils.command.upload import upload
from django import forms

class ProfileEditForm(forms.Form):
    name = forms.CharField(max_length=50, label='名前')
    profile = forms.CharField(label='自己紹介', widget=forms.Textarea())
    birthday = forms.DateField(label="生年月日")
    #icon = forms.ImageField(upload_to='???')

    def __str__(self):
        return self.name