from accounts.forms import DonateForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic.edit import CreateView
from .models import Donator
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Login(LoginView):
    template_name = 'accounts/login.html'

class Logout(LogoutView):
    template_name = 'accounts/logout.html'

class SignUp(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')

class Profile(CreateView):
    form_class = DonateForm
    template_name = 'accounts/profile.html'
    success_url = '/food/donate/'

def index(request):
    return render(request, 'accounts/index.html')