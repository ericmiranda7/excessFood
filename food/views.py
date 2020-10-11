from food.models import Food
from django.shortcuts import render
from .forms import FoodForm
from django.views.generic import CreateView

# Create your views here.
"""def donate(request):
    if request.method == 'GET':
        form = FoodForm()
        return render(request, 'food/donate.html', {'form': form})
    else:
        form = FoodForm(data=request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'food/success.html')"""

class Donate(CreateView):
    model = Food
    fields = ['name', 'category', 'qty', 'expiry', 'address']
    template_name = 'food/donate.html'

def display(request):
    pass
