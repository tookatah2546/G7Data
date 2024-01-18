from django.urls import path
from .views import group_list, create_group

urlpatterns = [
    path('groups/', group_list, name='group_list'),
    path('create_group/', create_group, name='create_group'),
    
]