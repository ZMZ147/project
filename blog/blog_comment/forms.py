from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        form=Comment
        fields=('name','email','body')