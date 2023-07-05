from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('registration/',views.reg,name='registration'),
    path('login/',views.signup,name='loginpage'),
    path('customer/',views.customer,name='customer'),
    path('update/<id>/',views.updateperson,name='updatepage'),
]
