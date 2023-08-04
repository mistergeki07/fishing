from django.forms import ModelForm
from django.forms import TextInput
from .models import *


class LoginForm(ModelForm):
    class Meta:
        model = Login

        fields = ['email', 'password']
        
        widgets = {
            "email": TextInput(attrs={
                "class": "input",
                "placeholder": "Email"
            }),
            "password": TextInput(attrs={
                "class": "input",
                "placeholder": "Password"
            })
        }