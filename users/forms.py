from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(required=False)
    role = forms.ChoiceField(choices=CustomUser.role_choices)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'age', 'role')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name', 'email', 'age', 'role', 'is_active', 'is_staff', 'is_superuser',
            'groups', 'user_permissions')
