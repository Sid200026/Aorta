from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginUser, name="loginuser"),
    path('signup/', views.RegUser, name="reguser"),
    path('signup/complete', views.completeaccount, name="completeaccount"),
    path('users/edit/', views.UpdateUser, name="updateuser"),
    path('user/dashboard/', views.dash, name="dashboard"),
    path('logout/', views.logout_view, name="logout"),
    path('user/account/', views.account, name="account"),
]
