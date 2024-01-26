
from django.shortcuts import render

# Create your views here.


def home(request):
    # โค้ดที่เกี่ยวกับหน้า home
    return render(request, 'home.html')

def create_project_group(request):
    # โค้ดที่เกี่ยวกับหน้า home
    return render(request, 'create_project_group.html')


