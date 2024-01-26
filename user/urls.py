from django.urls import path, include
from . import views
from .views import create_project_group

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path('create_project_group/', create_project_group, name='create_project_group'),
]