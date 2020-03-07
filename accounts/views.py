from django.shortcuts import render, redirect
from accounts.forms import *
from django.contrib.auth import authenticate, login


# Create your views here.

def home(request):
    return render(request,'base.html')

def register(request):
    form=Register()
    if request.method=='POST':
        form=Register(request.POST)
        if form.is_valid():
            form.save()

            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/')

    return render(request,'registration/register.html',{'form':form})
