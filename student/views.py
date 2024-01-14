from django.shortcuts import render, redirect
from student.forms import RegisterForm
from django.contrib.auth import authenticate, login



# Create your views here.
def register(request):
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'app_users/register.html', context)

def home(request):
    return render(request, 'index/home.html')

