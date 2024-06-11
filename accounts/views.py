from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomPasswordChangeForm

@login_required
def account_update(request):
    """
    Allows users to update their profile information.

    If the request method is POST and the user form is valid,
    updates the user profile information.
    """
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('account_update')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = CustomUserChangeForm(instance=request.user)

    password_form = CustomPasswordChangeForm(request.user)

    return render(request, 'accounts/account_admin.html', {
        'user_form': user_form,
        'password_form': password_form
    })

@login_required
def account_password_change(request):
    """
    Allows users to change their account password.

    If the request method is POST and the password form is valid,
    updates the user's password.
    """
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account_update')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        return redirect('account_update')

@login_required
def account_delete(request):
    """
    Allows users to delete their account.

    If the request method is POST and the password provided is correct,
    deletes the user account.
    """
    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(username=request.user.username, password=password)
        if user is not None:
            user.delete()
            messages.success(request, 'Your account was successfully deleted!')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect password. Please try again.')
            return redirect('account_delete')
    return render(request, 'accounts/account_admin.html')
