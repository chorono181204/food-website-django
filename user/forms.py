from contextlib import nullcontext

from django import forms
from .models import customer
from django.forms import ModelForm


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    confirmedPassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirmed Password'}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Age'}))
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender  '}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    phone_number=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
