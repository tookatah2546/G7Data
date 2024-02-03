from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from .forms import ProjectGroupForm
from .models import ProjectGroup
from rest_framework import viewsets
from .serializers import ProjectGroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

"""@login_required
def create_project_group(request):
    if request.method == 'POST':
        form = ProjectGroupForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            project_count = form.cleaned_data['project_count']

            # Get the logged-in user (assume it's the teacher)
            teacher = request.user

            # Auto create project groups linked to the teacher
            for i in range(project_count):
                group = ProjectGroup(subject=subject, teacher=teacher)
                group.save()

            return redirect('home') 
    else:
        form = ProjectGroupForm()

    return render(request, 'create_project_group.html', {'form': form})"""

# views.py

from .models import ProjectGroup
from .forms import ProjectGroupForm

def create_project_group(request):
    if request.method == 'POST':
        form = ProjectGroupForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            project_count = form.cleaned_data['project_count']

            # สร้าง group_id จาก subject
            group_id = subject[:3].upper()

            # ตรวจสอบว่า group_id ซ้ำหรือไม่
            existing_groups = ProjectGroup.objects.filter(group_id__startswith=group_id)
            if existing_groups.exists():
                group_id += str(existing_groups.count() + 1)

            # สร้างกลุ่มโปรเจกต์
            ProjectGroup.objects.create(
                subject=subject,
                project_count=project_count,
                group_id=group_id
            )

            return redirect('home')  # ให้ redirect ไปยังหน้าที่ต้องการ
    else:
        form = ProjectGroupForm()

    return render(request, 'create_project_group.html', {'form': form})


class TodoView(viewsets.ModelViewSet):
    serializer_class = ProjectGroupSerializer
    queryset = ProjectGroup.objects.all()

class TodoView(APIView):  # แก้นี้
    def get(self, request, *args, **kwargs):
        queryset = ProjectGroup.objects.all()
        serializer = ProjectGroupSerializer(queryset, many=True)
        return Response(serializer.data)    


