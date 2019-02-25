from .models import *
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uphone','upwd']
        labels = {'uphone':'手机号','upwd':'密码'}
        widgets = {
            'uphone':forms.TextInput(
                attrs={
                    'class':'uinput'
                }
            ),
            'upwd':forms.PasswordInput(
                attrs={
                    'placeholder':"请输入６－２０位字符",
                    'class':'uinput'
                }
            )

        }