from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class Login(LoginView):
    template_name = 'accounts/login.html'

class Logout(LogoutView):
    template_name = 'accounts/logout.html'

def signup(request):
    return render(request, 'accounts/signup.html')

def index(request):
    return render(request, 'accounts/index.html')