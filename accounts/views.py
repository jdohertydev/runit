from django.contrib.auth import update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, CustomPasswordChangeForm

# Create your views here.

@login_required
def account_update(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user = user_form.save()
            password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('account_update')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)
    return render(request, 'accounts/account_update.html', {
        'user_form': user_form,
        'password_form': password_form
    })

@login_required
def account_delete(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(username=request.user.username, password=password)
        if user is not None:
            user.delete()
            messages.success(request, 'Your account has been deleted.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid password. Please try again.')
    return render(request, 'accounts/account_delete.html')