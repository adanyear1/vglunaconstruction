"""
Definition of urls for vglunaconstruction.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('residential/', views.residential, name='residential'),
    path('commercial/', views.commercial, name='commercial'),
    path('inprogress/', views.inprogress, name='inprogress'),
    path('sanangelo/', views.sanangelo, name='sanangelo')
]
