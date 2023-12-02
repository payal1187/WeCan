from django.shortcuts import render
from .models import * 
from .forms import  ContactForm
from rest_framework.response import Response 
from rest_framework import generics
from myApp1.serializers import ContactSerializer


def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html",{'navbar':'contact'})

def about(request):
    return render(request, "about.html",{'navbar':'about'})

def contact_details(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        concern = request.POST.get('text')
        # member = request.POST.get('member')
        # if member == 'on':
        #     member = 'True'
        # else:
        #     member = 'False'
        data = ContactModel(email=email,concern=concern) #email(name of model field) = email(variable which gets the value from post method)
        data.save()
        return render(request, "contact.html")