from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from users.models import CustomUser
import datetime as dt
from .models import Patient,Doctor


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
			login(request,new_user)
			return HttpResponseRedirect(reverse('mainapp:completeaccount'))
		except:
			return render(request, 'mainapp/signup.html',{'isfail':None})
	else:
		return render(request, 'mainapp/signup.html',{'isfail':False})

@login_required
def completeaccount(request):
	if request.method == 'GET':
		if request.user.user_type == 'Patient':
			return render(request,'mainapp/patientcompleteaccount.html')
		elif request.user.user_type == 'Doctor' :
			return render(request,'mainapp/doctorcompleteaccount.html')	
		else:
			return HttpResponseRedirect(reverse('mainapp:reguser'))

	elif request.method == 'POST':
		if request.user.user_type == 'Patient':
			firstname=request.POST.get('firstname')
			lastname=request.POST.get('lastname')
			address=request.POST.get('address',default=None)
			phonenumber=request.POST.get('phonenumber',default=None)
			dateofbirth=request.POST.get('dateofbirth')
			age=dt.datetime.now().year-int(dateofbirth[0:4])
			sex=request.POST.get('sex')
			user=request.user
			patient_obj=Patient(user=user,firstname=firstname,lastname=lastname,dateofbirth=dateofbirth,address=address,phonenumber=phonenumber,age=age,sex=sex)
			if patient_obj :
				patient_obj.save()
				return HttpResponse('success')
			else:
				return HttpResponse('failure')

		elif request.user.user_type == 'Doctor':
			firstname=request.POST.get('firstname')
			lastname=request.POST.get('lastname')
			phonenumber=request.POST.get('phonenumber',default=None)
			user=request.user
			degrees=request.POST.get('degrees')
			registrationno=request.POST.get('registrationno')
			bio=request.POST.get('bio')
			doctor_obj=Doctor(user=user,firstname=firstname,lastname=lastname,phonenumber=phonenumber,degrees=degrees,registrationno=registrationno,bio=bio)
			if doctor_obj :
				doctor_obj.save()
				return HttpResponse('success')
			else:
				return HttpResponse('failure')
	else:
		return HttpResponse('Wrong method')