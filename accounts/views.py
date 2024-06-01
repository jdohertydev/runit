from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomPasswordChangeForm

@login_required
def account_update(request):
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
