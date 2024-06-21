from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import CustomUserChangeForm, CustomPasswordChangeForm
from django.conf import settings


@login_required
def account_update(request):
    if request.method == "POST":
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user = user_form.save()

            # Send email notification to the user
            send_mail(
                "Account Information Updated",
                "Your account information has been successfully updated.",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                html_message=render_to_string(
                    "emails/account_updated_email.html",
                    {"username": user.username, "site_name": "Your Website/App Name"},
                ),
                fail_silently=False,
            )

            messages.success(request, "Your profile was successfully updated!")
            return redirect("account_update")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        user_form = CustomUserChangeForm(instance=request.user)

    password_form = CustomPasswordChangeForm(request.user)

    return render(
        request,
        "accounts/account_admin.html",
        {"user_form": user_form, "password_form": password_form},
    )


@login_required
def account_password_change(request):
    if request.method == "POST":
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!

            # Render email content from template
            context = {
                "username": user.username,
                "site_name": settings.SITE_NAME,  # Replace with your site name or retrieve dynamically
            }
            html_message = render_to_string(
                "emails/password_changed_email.html", context
            )
            plain_message = strip_tags(
                html_message
            )  # Strip HTML tags for plain text email

            # Send email notification to the user
            send_mail(
                "Password Changed",
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                html_message=html_message,
                fail_silently=False,
            )

            messages.success(request, "Your password was successfully updated!")
            return redirect("account_update")
        else:
            messages.error(request, "Please correct the error below.")
            # Return a response even when the form is not valid
            return render(
                request,
                "accounts/account_admin.html",
                {
                    "password_form": password_form,
                },
            )

    # Handle GET requests (initial form display)
    password_form = CustomPasswordChangeForm(request.user)
    return render(
        request,
        "accounts/account_admin.html",
        {
            "password_form": password_form,
        },
    )


@login_required
def account_delete(request):
    if request.method == "POST":
        password = request.POST.get("password")
        user = authenticate(username=request.user.username, password=password)
        if user is not None:
            # Render email content from template
            context = {
                "username": user.username,
                "site_name": settings.SITE_NAME,  # Replace with your site name or retrieve dynamically
            }
            html_message = render_to_string(
                "emails/account_deleted_email.html", context
            )
            plain_message = strip_tags(
                html_message
            )  # Strip HTML tags for plain text email

            # Send email notification to the user
            send_mail(
                "Account Deleted",
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                html_message=html_message,
                fail_silently=False,
            )

            user.delete()
            messages.success(request, "Your account was successfully deleted!")
            return redirect("landing_page")
        else:
            messages.error(request, "Incorrect password. Please try again.")
            return redirect("account_delete")

    return render(request, "accounts/account_admin.html")
