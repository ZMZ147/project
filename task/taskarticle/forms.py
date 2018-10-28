from django import forms
from .models import *


class articleform(forms.ModelForm):
    class Meta:
        model=ArticleInfo
        fields=('title','content')


class commentform(forms.ModelForm):

    content=forms.CharField(widget=forms.TextInput(attrs={'rows':4,'clos':65}))

    class Meta:
        model=Comment
        fields=('content',)


class  tagform(forms.ModelForm):
    class Meta:
        model=tag
        fields=('tag',)