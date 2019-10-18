from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from manager.models import Manager
from itertools import chain
from user_profile.models import Order
from django.http import JsonResponse

@login_required
def index(request):
    user=request.user
    if user.is_superuser:
        users=User.objects.exclude(id=user.id)
    elif user.is_staff==False:
        managers=Manager.objects.all()
        admin=User.objects.filter(is_superuser=True)
        users=chain(admin,managers)
    else:
        orders=Order.objects.filter(manager=user)
        users=[order.user for order in orders]
    return render(request,'chat/index.html',{'users':users,})

@login_required
def get_messages(request,id):
    if request.is_ajax():
        return JsonResponse({'ok':'ok'})