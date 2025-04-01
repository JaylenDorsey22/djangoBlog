from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()

## Meta Class Inside the form is used to configure how the form 
## will behave.
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

