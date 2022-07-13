from django import forms
from .models import *


class ArticleForm(forms.ModelForm):
    body_text = forms.CharField(widget=forms.Textarea, label='Write Main Body Here')
    title = forms.CharField(max_length=250, label='Title')
    author = forms.CharField(max_length=100, label='Title')

    class Meta:
        model = Article
        fields = ('title', 'body_text')
