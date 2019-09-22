from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

def register(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'user_profile/orders.html',{'user':new_user})
    else:
        user_form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':user_form})


@login_required
def orders(request):
    return render(request,'user_profile/orders.html',{'1':1})
