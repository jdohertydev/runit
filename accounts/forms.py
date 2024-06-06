from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class CustomUserChangeForm(UserChangeForm):
    password = None  # Hide the password field

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        help_texts = {
            'username': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
