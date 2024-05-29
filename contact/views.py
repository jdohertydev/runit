from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactForm

@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email to superuser
            send_mail(
                subject=f'Message from {name}',
                message=message,
                from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )
            
            messages.success(request, 'Your message has been sent successfully.')
            return render(request, 'contact/contact.html', {'form': form})
    else:
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.get_full_name(),
                'email': request.user.email,
            }
            form = ContactForm(initial=initial_data)
        else:
            form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})

