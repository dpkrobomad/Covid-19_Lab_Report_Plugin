from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('id/',include(views.get_report)),
]
