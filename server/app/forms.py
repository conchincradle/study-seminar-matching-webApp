from django import forms
from .models import AppComment, StudyComment

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())

class CommentForm(forms.ModelForm):
    class Meta:
        model = AppComment
        fields = ['content']

class CommentStudyForm(forms.ModelForm):
    class Meta:
        model = StudyComment
        fields = ['content']

class PostStudyForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())
    link = forms.CharField(max_length=30, label='URL')