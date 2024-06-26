# utils.py
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_signup_confirmation_email(user, post):
    """
    Sends a signup confirmation email to the user.
    """
    email_context = {
        "user": user,
        "post": post,
    }
    email_html_message = render_to_string(
        "email/signup_confirmation_email.html", email_context
    )
    send_mail(
        "Event Signup Confirmation",
        "",
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,  # This controls whether exceptions are raised on email sending errors
        html_message=email_html_message,
    )


def send_unregistration_confirmation_email(user, post):
    """
    Sends an unregistration confirmation email to the user.
    """
    email_context = {
        "user": user,
        "post": post,
    }
    email_html_message = render_to_string(
        "email/unregistration_confirmation_email.html", email_context
    )
    send_mail(
        "Event Unregistration Confirmation",
        "",
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,  # This controls whether exceptions are raised on email sending errors
        html_message=email_html_message,
    )
