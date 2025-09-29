from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string


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
        subject1 = request.POST.get('subject')

        Contact.objects.create(
            name = name,
            email = email,
            message = message,
            subject1 = subject1,
        )
        subject = "Thank you for contacting us"
        message = render_to_string('portapp/msg.html',{
            'name': name,
            'subject1': subject1,
        })
        
        from_email = 'khatripujan35@gmail.com'#sender's email-id
        recipient_list = [email] #receiver's email-id
        msg_email = EmailMessage(subject,message,from_email,recipient_list)
        msg_email.send(fail_silently=True)

        

    return render(request,'portapp/contact.html')


def about(request):
    return render(request,'portapp/about.html')