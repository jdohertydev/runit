from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save the message to the database
            ContactMessage.objects.create(name=name, email=email, message=message)
            
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')  # Redirect to the same page after successful submission
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
