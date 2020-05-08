from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def service(request):
    return render(request, 'service.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name, #subject
            message, # message
            message_email, # FROM email
            [''], # TO email
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})