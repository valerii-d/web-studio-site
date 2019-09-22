from django.urls import path, include
from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns=[
    path('register/',views.register,name="register"),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(template_name=''), name='logout'),
    path('orders/',views.orders,name="orders"),
]