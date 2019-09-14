from django.urls import path
from . import views

app_name='mainapp'

urlpatterns=[
	path('login/', views.loginUser, name="loginuser"),
	path('signup/', views.RegUser, name="reguser"),
	path('signup/complete',views.completeaccount,name="completeaccount")
]