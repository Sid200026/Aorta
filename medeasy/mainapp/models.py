from django.db import models
from users.models import CustomUser
import datetime


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    phonenumber = models.CharField(max_length=10, blank=False)
    degrees = models.CharField(max_length=50, blank=False)
    iscertified = models.BooleanField(default=False)
    registrationno = models.CharField(max_length=30)
    bio = models.CharField(max_length=100)
    numberofpatients = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    dateofbirth = models.CharField(max_length=10, blank=False)
    address = models.CharField(max_length=100, default=None, blank=True)
    phonenumber = models.CharField(max_length=10, default=None, blank=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=6, blank=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username


class ModelReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_content = models.CharField(max_length=500)

    def __str__(self):
        return self.patient.user.username


class ModelTwoReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_content = models.CharField(max_length=500)

    def __str__(self):
        return self.patient.user.username


class Notifications(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hasNotification = models.BooleanField(default=False)
    msg = models.CharField(max_length=400)

    def __str__(self):
        return self.patient.user.username + '    '+self.doctor.user.username
