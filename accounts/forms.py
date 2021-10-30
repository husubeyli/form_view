from django import forms
from django.forms import fields
from django.utils.translation import ugettext_lazy as _

from .models import Consumer



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = [
            'email',
            'position',
            'position_info',
            'deadline',
        ]
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': _('Enter your email here'),
                'id': "form3Example1q",
                'class': "form-control"
            }),
            'position': forms.TextInput(attrs={
                'placeholder': _('Enter your position'),
                'id': "position",
                'class': "form-control"
            }),
            'position_info': forms.Textarea(attrs={
                'placeholder': _('Enter your position info'),
                'id': "position_info",
                'class': "form-control",
                'cols': 50,
                'rows': 10
            }),
            'deadline': forms.DateTimeInput(format=["%Y-%m-%d %H:%M:%S", ], attrs={
                'id':'deadline', 
                'placeholder': _('years-month-days h:m'), 
            }),

        }



class LoginForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = [
            'secret_key'
        ]
        widgets = {
            'secret_key': forms.TextInput(attrs={
                'placeholder': _('Secret key'),
                'class': "form-control",
                'style': "width: 100%",
            }),

        }