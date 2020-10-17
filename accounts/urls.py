from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('volunteerProfile/', views.VolunteerProfile.as_view(), name='volunteerProfile'),
    path('points/', views.points, name='points'),
    path('', views.index)
]