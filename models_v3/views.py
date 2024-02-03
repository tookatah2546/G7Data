from django.shortcuts import render
from student.forms import RegisterForm


# Create your views here.
def register(request):
    form = RegisterForm
    context = {'form': form}
    return render(request, 'app_users/register.html', context)