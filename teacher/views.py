from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, 'index/home.html')


