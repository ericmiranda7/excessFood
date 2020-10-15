from food.views import Donate
from django.urls import path
from . import views

urlpatterns = [
    path('donate/', Donate.as_view(), name='donate'),
    path('display/', views.display),
    path('success/', views.success),
]