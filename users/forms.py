from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', ]


class UserVerificationForm(forms.Form):
    code = forms.CharField(max_length=4, min_length=4)
