from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def index(request):
    form = ContactForm(request.POST)

    return render(request, 'index.html', {'form':form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            name = form.cleaned_data['contact_name']
            email = form.cleaned_data['contact_email']
            subject = form.cleaned_data['contact_subject']
            message = form.cleaned_data['contact_message']

            # Send the email
            send_mail(
                subject if subject else f"Message from {name}",
                message,
                email,  # sender's email
                [settings.CONTACT_EMAIL],  # recipient email defined in settings.py
                fail_silently=False,
            )

            # Return success message or redirect
            return render(request, 'contact_success.html')

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})