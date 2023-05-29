# -*- coding: utf-8 -*-
from .models import Users
from django.forms import ModelForm, TextInput

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['nickname', 'password']

        # widgets = {
        #     "nickname": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Nikname'
        #     }),
        #     "password": TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Пароль'
        #     })
        # }