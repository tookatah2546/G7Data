from .views import register
from django.urls import path, include



urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]