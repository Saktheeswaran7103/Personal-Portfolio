
from django.shortcuts import render, redirect,HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    from datetime import date
    cover_context = {
        'today': date.today().strftime('%Y-%m-%d'),
        'company': 'Recruiter',
        'hiring_manager': 'Recruiter'
    }
    if request.method == "POST":
        contact_form = Contact_Form(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            context = {'contact_form': Contact_Form(), 'success': True, **cover_context}
        else:
            context = {'contact_form': contact_form, 'success': False, **cover_context}
    else:
        context = {'contact_form': Contact_Form(), **cover_context}
    return render(request, 'home.html', context)


def project(request):
    return render(request, 'project.html')


def project1(request):
    return render(request, 'project1.html')



def contact(request):
    #contact form database
    """if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()"""
    return render(request, 'home.html')




