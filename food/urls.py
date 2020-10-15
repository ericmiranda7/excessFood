from food.views import Donate, FoodList
from django.urls import path
from . import views

urlpatterns = [
    path('donate/', Donate.as_view(), name='donate'),
    path('display/', FoodList.as_view(), name='display'),
    path('success/', views.success),
]