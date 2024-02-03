# urls.py
from django.urls import path
from .views import TodoView
#from .views import create_project_group

urlpatterns = [
     path('projectall/', TodoView.as_view(), name='TodoView'),
    # path('create_project_group/', create_project_group, name='create_project_group'),
    # เพิ่ม URL patterns อื่นๆ ตามที่คุณต้องการ
]
