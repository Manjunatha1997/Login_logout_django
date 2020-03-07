from django import forms

from django.contrib.auth.forms import UserCreationForm,User

class Register(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1','password2']

