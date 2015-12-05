__author__ = 'Hernan Y.Ke'
from django import forms

class LoinForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)