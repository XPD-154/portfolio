from django.shortcuts import render, redirect
from .models import *                   #import all models into view
#from .utils import *                    #import all functions into view
from django.http import JsonResponse
import requests
import json
import datetime
import decimal
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib import messages

# Create your views here.

#method to handle about page display
def index(request):
    skills = Skills.objects.all()
    information = Information.objects.all()
    projects = Projects.objects.all()
    
    if request.method == "POST":
        contact = Contact_us()
        name = request.POST.get('contact_name')
        email = request.POST.get('contact_email')
        message = request.POST.get('contact_message')
        
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        
        messages.success(request, 'Message has been sent successfully.')
        
        return redirect('index')
    
    context = {'skills':skills, 'information':information, 'projects':projects}
    return render(request, 'base/index.html', context)