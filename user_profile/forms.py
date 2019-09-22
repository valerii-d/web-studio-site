from django import forms
from django.contrib.auth.models import User
from .models import Order

class UserRegistrationForm(forms.ModelForm): 
    first_name=forms.CharField(label='First name',required=True)
    last_name=forms.CharField(label='Last name',required=True)
    email=forms.EmailField(label='Email',widget=forms.EmailInput,required=True)
    password=forms.CharField(label='Password',widget=forms.PasswordInput,required=True)
    password2=forms.CharField(label='Reapeat password',widget=forms.PasswordInput,required=True)

    class Meta:
        model=User
        fields=('username',)

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['password2']


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('description','deadline')


