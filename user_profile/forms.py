from django import forms
from django.contrib.auth.models import User
from .models import Order
from django.utils import timezone
from .validators import validate_deadline
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    username=forms.CharField(label='Username',required=True,widget=forms.TextInput(attrs={'placeholder': 'Username'})) 
    first_name=forms.CharField(label='First name',required=True,widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name=forms.CharField(label='Last name',required=True,widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email=forms.EmailField(label='Email',required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password=forms.CharField(label='Password',required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2=forms.CharField(label='Reapeat password',required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Reapeat password'}))

    class Meta:
        model=User
        fields=('username',)

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']

class OrderCreationForm(forms.ModelForm):
    deadline=forms.DateTimeField(label='Deadline',widget=forms.DateTimeInput,validators=(validate_deadline,),initial=timezone.now())

    class Meta:
        model=Order
        fields=('description',)


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))