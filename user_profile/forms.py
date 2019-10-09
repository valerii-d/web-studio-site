from django import forms
from django.contrib.auth.models import User
from .models import Order
from django.utils import timezone
from .validators import validate_deadline
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import ValidationError

class UserRegistrationForm(forms.ModelForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder': 'Username'})) 
    first_name=forms.CharField(label='First name',widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name=forms.CharField(label='Last name',widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2=forms.CharField(label='Reapeat password',widget=forms.PasswordInput(attrs={'placeholder': 'Reapeat password'}))

    class Meta:
        model=User
        fields=('username','email','first_name','last_name',)

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']

class OrderCreationForm(forms.ModelForm):
    deadline=forms.DateTimeField(
    label='Deadline',
    widget=forms.DateTimeInput(),
    validators=(validate_deadline,),initial=timezone.now())

    def validate_deadline(value):
        if value!=timezone.now():
            return ValidationError("The date cannot be in the past!")
    class Meta:
        model=Order
        fields=('description',)


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))