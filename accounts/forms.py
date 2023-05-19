from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class loginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
