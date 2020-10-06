from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
    path('', views.index)
]