from django.urls import path
from .views import create_daily_scrum, daily_scrum_list

urlpatterns = [
    path('daily/', create_daily_scrum, name='daily'),
    path('daily/list/', daily_scrum_list, name='daily_scrum_list'),
]