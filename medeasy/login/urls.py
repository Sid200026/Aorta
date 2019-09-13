from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('login/', views.loginUser, name="loginUser"),
    path('signup/', views.RegUser, name="reguser")
]
