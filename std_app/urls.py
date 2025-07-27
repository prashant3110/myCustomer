from django.contrib import admin
from django.urls import path
from std_app import views

urlpatterns = [
    path("home/",views.HomePage,name='home'),
    path("about/",views.AboutUS,name='about'),
    path("services/",views.Services,name='services'),
    path("addstd/",views.Add_Std,name='addstd'),
    path("edit/<int:id>/",views.EditStd,name='edit'),
    path("delete/<int:id>/",views.DeleteStd,name='delete'),
]