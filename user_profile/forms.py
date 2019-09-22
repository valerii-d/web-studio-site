from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    r_password=forms.CharField(label='Reapeat password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','first_name','last_name','email')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['r_password']:
            raise forms.ValidationError('Password don\'t match.')
        return cd['r_password']
