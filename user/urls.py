from django.contrib import admin
from django.urls import path
from . import views


app_name="user"

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('profile/',views.profileUser,name="profile"),
    path('addprofile/',views.addProfile,name="addprofile"),
    path('editprofile/',views.editProfile,name="editprofile"),

    
]