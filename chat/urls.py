from django.shortcuts import render
from django.urls import path
from . import views

app_name="chat"

urlpatterns=[
    path('chat/',views.index,name='index'),
    path('chat/<int:id>/',views.get_messages,name='messages'),
]