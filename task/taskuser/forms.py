

from django import forms

from django.forms import fields

class user_register(forms.Form):
    username=forms.CharField(label='用户',widget=forms.TextInput,
                             max_length=10,min_length=2,
                             error_messages={'required':'不能为空','max_length':'最长不能超过10' })

    pw1=forms.CharField(label='密码',widget=forms.PasswordInput)

    pw2=forms.CharField(label='密码2',widget=forms.PasswordInput)

class user_login(forms.Form):
    username = forms.CharField(label='用户', widget=forms.TextInput)

    password = forms.CharField(label='密码', widget=forms.PasswordInput)

    check_code=forms.CharField(widget=forms.TextInput)












