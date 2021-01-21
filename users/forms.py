from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Форма регистрации юзера"""
    class Meta:
        model = CustomUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    """Форма регистрации юзера"""
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
