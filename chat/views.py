from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from manager.models import Manager
from itertools import chain
from user_profile.models import Order
from django.http import JsonResponse, Http404
from .models import Message, Chat
from django.shortcuts import get_object_or_404

app_name = 'chat'

@login_required
def index(request):
    user = request.user
    chats = Chat.objects.filter(users=user)
    f_user=chats[0].users.exclude(id=user.id)[0]
    # f_user=User.objects.exclude(id=user.id)[0]
    messages=chats[0].messages.all()
    return render(request,'chat/index.html',{'chats':chats,'f_user':f_user,'messages':messages})

@login_required
def get_messages(request, id):
    chat=get_object_or_404(Chat,pk=id)
    sender = request.user
    if request.method=='GET' and request.is_ajax():
        receiver=chat.users.exclude(id=sender.id)[0]
        messages=chat.messages.values()
        return JsonResponse({
        'chat_id': chat.id,
        'sender_id': sender.id,
        'receiver_f': receiver.first_name,
        'receiver_l': receiver.last_name,
        'receiver_email':receiver.email,
        'results': list(messages)})
    elif request.method=='POST' and request.is_ajax():
        data=request.POST.get('message')
        message=Message(message=data,user=sender)
        message.save()
        chat.messages.add(message)
        return JsonResponse({'message':message.message,'created':message.created})
    return Http404()
