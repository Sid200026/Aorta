from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser


# Create your views here.

def loginUser(request):
	context = {'error':'Wrong Username or Password'}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return HttpResponse(user.user_type)
		else:
			return render(request, 'mainapp/login.html', context)
	else:
		return render(request, 'mainapp/login.html')


# Add the radio button to get the type of user in both the html and the func below

def RegUser(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		usertype = request.POST.get('usertype')
		try:
			new_user = CustomUser.objects.create_user(username=username,email=email,password=password,user_type=usertype)
			return render(request, 'mainapp/signup.html',{'isfail':False})
		except:
			return render(request, 'mainapp/signup.html',{'isfail':True})
	else:
		return render(request, 'mainapp/signup.html',{'isfail':False})
