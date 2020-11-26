from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("aboutme", views.aboutme, name='aboutme'),
    path("myskillset", views.myskillset, name='myskillset'),
    path("contact", views.contact, name='contact'),
    path("mywork", views.mywork, name='mywork'),
    path("downloadResume", views.downloadResume,name='test'),


]