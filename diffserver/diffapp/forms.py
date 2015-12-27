# coding: utf-8


from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(u'Login')
    password = forms.CharField(u'Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(u'Password (again)', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('User "%s" is already registered' % username)
        pw = cleaned_data.get('password')
        pw2 = cleaned_data.get('repeat_password')
        if pw and pw2 and pw != pw2:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data
