from django.db import models
from users.models import CustomUser
import datetime

class Patient(models.Model):
	user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	firstname=models.CharField(max_length=50,blank=False)
	lastname=models.CharField(max_length=50,blank=False)
	dateofbirth=models.CharField(max_length=10,blank=False)
	address=models.CharField(max_length=100,blank=False)
	phonenumber=models.CharField(max_length=10)
	profilepicture=models.ImageField(upload_to='profileimages/')
	age=models.IntegerField()
	weight=models.IntegerField()
	height=models.IntegerField()
	sex=models.CharField(max_length=6,choices=[('Male','Male'),('Female','Female'),('Other','Other')],blank=False)

	def __str__(self):
		return user.username

class Doctor(models.Model):

	user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
	firstname=models.CharField(max_length=50,blank=False)
	lastname=models.CharField(max_length=50,blank=False)
	profilepicture=models.ImageField(upload_to='profileimages/')
	phonenumber=models.CharField(max_length=10,blank=False)
	degrees=models.CharField(max_length=50,blank=False)
	iscertified=models.BooleanField(default=False)
	registrationno=models.CharField(max_length=30)
	bio=models.CharField(max_length=100)

	def __str__(self):
		return user.username