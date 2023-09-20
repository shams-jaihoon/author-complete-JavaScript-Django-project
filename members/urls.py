from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('about', views.about, name='about'),
]