from django.contrib import admin
from django.urls import path, include
from Aditi import views

urlpatterns = [
    path('', views.Aditi, name='Aditi'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
]