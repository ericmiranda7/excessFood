from typing import List
from food.models import Food
from django.shortcuts import render
from .forms import FoodForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date

# Helper functions
import math

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

# Create your views here.
class Donate(LoginRequiredMixin, CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food/donate.html'
    success_url = '/food/success/'
    
    def get_initial(self, **kwargs):
        initial = super(Donate, self).get_initial(**kwargs)
        initial['donator'] = self.request.user.donator
        return initial



class FoodList(ListView):
    model = Food
    paginate_by = 8
    ordering = ['expiry', 'distance']

    

def success(request):
    return render(request, 'food/success.html')


