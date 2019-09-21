from django.urls import path, include

urlpatterns=[
    path('profile/',include('django.contrib.auth.urls')),
]