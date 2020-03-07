from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from accounts.views import *
from django.contrib import messages

urlpatterns=[
    path('',home),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('register/',register),

]