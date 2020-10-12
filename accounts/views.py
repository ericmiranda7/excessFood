from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .models import Donator
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Login(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        donator = Donator(user=form.get_user())
        donator.save()
        return HttpResponseRedirect(self.get_success_url())

class Logout(LogoutView):
    template_name = 'accounts/logout.html'

class SignUp(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm

def index(request):
    return render(request, 'accounts/index.html')