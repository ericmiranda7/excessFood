from typing import List
from food.models import Food
from django.shortcuts import render
from .forms import FoodForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date

#Geoloc
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from decimal import Decimal

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

    def form_valid(self, form):
        donator = self.request.user.donator
        donator.points += 1
        donator.save()
        form.save()
        return super(Donate, self).form_valid(form)



class FoodList(ListView):
    model = Food
    paginate_by = 9

    def get_queryset(self, **kwargs):
        userLocation = self.request.user.donator.location
        if self.request.GET.get('lat') is not None:
            print("YA MANNNNNNNNNNNN BROWSER LOC")
            lat = float(self.request.GET.get('lat'))
            print(lat)
            lon = float(self.request.GET.get('lon'))
            print(userLocation)
            userLocation = Point(lat, lon, srid=4326)
            print(userLocation)
        if userLocation:
            print(userLocation)
            print('using top')
            qs = Food.objects.annotate(distance=Distance('location', userLocation)).order_by('expiry', 'distance')
        else:
            qs = Food.objects.all().order_by('expiry')
        return qs

    
def success(request):
    return render(request, 'food/success.html')


