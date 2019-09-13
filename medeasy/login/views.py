from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PatDocUser
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm


# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # Do a redirect
    return render(request, 'login/login.html')


# Add the radio button to get the type of user in both the html and the func below

def RegUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Get all 3 fields, put in form, validate and then store
    return render(request, 'login/signup.html')
