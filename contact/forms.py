from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    """
    Form for sending webmaster email.
    """

    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
