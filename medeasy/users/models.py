from django.db import models
# from django.contrib.auth.models import User, UserManager
from django.contrib.auth.models import AbstractUser

# class CustomUser(User):
#     # Add custom field
#     user_type = models.CharField(max_length=10,blank=False)
#     # Use UserManager to get the create_user method 
#     objects = UserManager()

# class CustomUser(models.Model):
# 	user=models.ForeignKey(User,on_delete=models.CASCADE)
# 	user_type=models.CharField(max_length=10,blank=False)

class CustomUser(AbstractUser):
    user_type=models.CharField(max_length=10,blank=False)