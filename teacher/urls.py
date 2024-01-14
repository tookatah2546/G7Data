from django.urls import path, include

# from teacher.views import some_view


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    
]