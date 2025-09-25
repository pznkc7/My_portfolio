from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request,'portapp/home.html')


def certificate(request):

    certificates = Certificate.objects.all() #retrieve all objects of certificate model
    context = {
        'certificates': certificates
    }
    return render(request, 'portapp/certificate.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')

        Contact.objects.create(
            name = name,
            email = email,
            message = message,
            subject = subject,
        )
    return render(request,'portapp/contact.html')


def about(request):
    return render(request,'portapp/about.html')