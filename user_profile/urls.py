from django.urls import path, include
from django.contrib import auth
from django.contrib.auth.views import LoginView
from . import views

urlpatterns=[
    path('register/',views.register,name="register"),
    path('login/',views.Login.as_view(), name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('orders/<path>',views.download,name='download'),
    path('orders/',views.orders,name='orders'),
    path('order/',views.order, name='create_order'),
    path('order/<int:id>/',views.revoke_order,name="order"),
]