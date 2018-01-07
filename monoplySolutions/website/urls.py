__author__ = 'christian.cecilia1@gmail.com'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactform/send/', views.contactFormSend, name='contactFormSend')
]
