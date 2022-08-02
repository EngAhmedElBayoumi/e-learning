
from django import forms
#from . import models
from django.contrib.auth.models import User
from .models import Profile




class LoginForm(forms.ModelForm):
     username = forms.CharField(label='اسم المستخدم')
     password = forms.CharField(label='كلمه المرور ' , widget=forms.PasswordInput())
     class Meta:
         model = User
         fields = ('username','password')        
class registrationForm(forms.ModelForm):
     username= forms.CharField(max_length=100)      
     first_name= forms.CharField(max_length=100)
     first_name= forms.CharField(max_length=100)      
     password= forms.CharField(max_length=100)     
     email= forms.EmailField(max_length=100)     
     phone= forms.CharField(max_length=100)     
     model=User
     field=('first_name','last_name','email')




