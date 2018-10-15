from django import forms
from .models import *

class  Email(forms.Form):
    name=forms.CharField(max_length=200)
    mail=forms.EmailField()
    to=forms.EmailField()
    content=forms.CharField(max_length=200,widget=forms.Textarea)


