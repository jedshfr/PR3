
from django.contrib import admin
from django.urls import path
from PR_3 import views

urlpatterns = [
    path('', views.first_page),
]
