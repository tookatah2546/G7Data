from django.shortcuts import render, redirect
from student.forms import RegisterForm
from django.contrib.auth import authenticate, login



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # ให้ไปที่หน้า home หลังจาก Sign In สำเร็จ
            else:
                # แสดงข้อความผิดพลาดหรือกระทำที่เหมาะสม
                pass
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'app_users/register.html', context)