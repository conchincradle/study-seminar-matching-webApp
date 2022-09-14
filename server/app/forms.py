from django import forms
from .models import AppComment

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())

class CommentForm(forms.ModelForm):
    class Meta:
        model = AppComment
        fields = ['content', 'author_id']