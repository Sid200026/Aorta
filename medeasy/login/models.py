from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class PatDocUser(models.Model):
    patient_user = models.OneToOneField(User, on_delete=models.CASCADE)
    isDoctor = models.BooleanField(default=False)

    def __str__(self):
        return "User" + self.user.username