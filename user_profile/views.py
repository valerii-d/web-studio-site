from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, OrderCreationForm
from .models import Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    if request.method=='POST':
        pass
        
    else:
        orders_list=Order.objects.all()
        paginator=Paginator(orders_list,2)
        page=request.GET.get('page')
        try:
            orders=paginator.page(page)
        except PageNotAnInteger:
            orders=paginator.page(1)
        except EmptyPage:
            orders=paginator.page(paginator.num_pages)
    return render(request,'user_profile/orders.html',{'orders':orders})

@login_required
def order(request):
    if request.method=='POST':
       order_form=OrderCreationForm(request.POST)
       if order_form.is_valid():
           new_order=order_form.save(commit=False)
           new_order.user=request.user
           new_order.save()
           return redirect('orders')
    else:
        order_form=OrderCreationForm()
    return render(request,'user_profile/order.html',{'form':order_form})