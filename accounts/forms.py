from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class CustomUserChangeForm(UserChangeForm):
    """
    Form to customize user profile editing.

    This form extends UserChangeForm to hide the password field and make the username field readonly.
    """

    password = None  # Hide the password field

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        help_texts = {
            "username": "",
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with customized attributes.

        Makes the username field readonly.
        """
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["readonly"] = True


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Form to customize password change.

    This form extends PasswordChangeForm.
    """

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
