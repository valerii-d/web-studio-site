from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserRegistrationForm, OrderCreationForm
from .models import Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CustomAuthForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse, Http404
import os
from django.conf import settings

user_login_required=user_passes_test(lambda user: user.is_staff==False and user.is_superuser==False, login_url='/login')

def non_staff_user_required(view_func):
    decorated_view_func=login_required(user_login_required(view_func))
    return decorated_view_func


def register(request):
    if request.method=='POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            if new_user is not None:
                if new_user.is_active:
                    login(request, new_user)
                    return redirect('orders')
                else:
                    return redirect('register')
    else:
        user_form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':user_form})

@non_staff_user_required
def logout_view(request):
    logout(request)
    return redirect('/')

@non_staff_user_required
def orders(request):
    if request.method=='POST':
        pass    
    else:
        orders_list=Order.objects.filter(user_id=request.user.id)
        paginator=Paginator(orders_list,2)
        page=request.GET.get('page')
        try:
            orders=paginator.page(page)
        except PageNotAnInteger:
            orders=paginator.page(1)
        except EmptyPage:
            orders=paginator.page(paginator.num_pages)
    return render(request,'user_profile/orders.html',{'orders':orders})

@non_staff_user_required
def order(request):
    if request.method=='POST':
       order_form=OrderCreationForm(request.POST)
       if order_form.is_valid():
           new_order=order_form.save(commit=False)
           new_order.user=request.user
           new_order.deadline=order_form.cleaned_data['deadline']
           new_order.save()
           return redirect('orders')
    else:
        order_form=OrderCreationForm()
    return render(request,'user_profile/order.html',{'form':order_form})

@non_staff_user_required
def revoke_order(request,id):
    order=get_object_or_404(Order,pk=id)
    if request.method=="POST":
        order.status='deviation'
        order.save()
        return redirect('orders')
    else:
        return render(request,'user_profile/detail.html',{'order':order})

class Login(LoginView):
    authentication_form=CustomAuthForm
    template_name='registration/login.html'

@non_staff_user_required
def download(request,path):
    if request.method=='POST':
        file_path=os.path.join(settings.BASE_DIR,'media/'+path)
        if os.path.exists(file_path):
            with open(file_path,'rb') as fh:
                response=HttpResponse(fh.read())
                response['Content-Disposition'] = 'attachment; filename='+os.path.basename(file_path)
                return response
    raise Http404