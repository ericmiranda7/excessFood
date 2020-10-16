from typing import List
from food.models import Food
from django.shortcuts import render
from .forms import FoodForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date

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

def success(request):
    return render(request, 'food/success.html')
