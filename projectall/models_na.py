from django.db import models
from django.contrib.auth.models import User

# วิชา
class Subject(models.Model):
    name = models.CharField(max_length=255)

# อาจารย์
class Teacher(models.Model):
    name = models.CharField(max_length=255)    

# นิสิต
class Student(models.Model):
    student_id = models.CharField(max_length=8, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group_student = models.CharField(max_length=255) #กลุ่ม(ของนิสิต)

# กลุ่มที่อาจารย์สร้าง
class ProjectGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    project_count = models.PositiveIntegerField(default=0)
    members = models.CharField(max_length=255) #นิสิต
    teacher = models.CharField(max_length=255) #อาจารย์

# Backlog
class ProductBacklog(models.Model):
    group_Backlog = models.CharField(max_length=255) #กลุ่ม(ของนิสิต)
    backlog_id = models.CharField(max_length=255)
    backlog_name = models.CharField(max_length=255)
    date_to_done = models.DateField(blank=True, null=True)
    STATUS_CHOICES = (
        ('todo', 'ต้องทำ'),
        ('doing', 'กำลังทำ'),
        ('done', 'เสร็จสิ้น'),
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='todo')
    date_done = models.DateField(blank=True, null=True)
    IMPORTANCE_CHOICES = (
        ('low', 'ต่ำ'),
        ('mid', 'ปานกลาง'),
        ('hight', 'มาก'),
    )
    importance = models.CharField(max_length=3, choices=IMPORTANCE_CHOICES, default='low')
    backloc_task = models.CharField(max_length=255) #addtask on backlog

# Task
class Task(models.Model):
    product_backlog = models.CharField(max_length=255) #product backlog
    task_id = models.CharField(max_length=255)
    task_name = models.CharField(max_length=255)
    detail = models.CharField(max_length=1000)
    # t_member = model. #นิสิตทำtask
    STATUS_CHOICES = (
        ('todo', 'ต้องทำ'),
        ('doing', 'กำลังทำ'),
        ('done', 'เสร็จสิ้น'),
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='todo')
    t_date_to_done = models.DateField(blank=True, null=True)
    t_date_done = models.DateField(blank=True, null=True)

# Daily Scrum (form)
class DailyScrum(models.Model):
    pj_group = models.ForeignKey(ProjectGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    yesterday = models.CharField(max_length=1000)
    today = models.CharField(max_length=1000)
    problem = models.CharField(max_length=1000)
    NOTE_CHOICES = [
        ('work', 'วันนี้ทำงาน'),
        ('sick', 'ป่วย'),
        ('busy.', 'ติดธุระ'),
        ('pass', 'ตกลงกันว่าวันนี้ไม่ทำงาน'),
        ('other', 'อื่นๆ (โปรดระบุ)'),
    ] 
    note = models.CharField(max_length=5, choices=NOTE_CHOICES)
    note_other = models.TextField(max_length=255)

# รายละเอียดกลุ่ม
class ProjectDetail(models.Model):
    project_name = models.CharField(max_length=255)
    trello_link = models.URLField(blank=True, null=True)
    figma_link = models.URLField(blank=True, null=True)
    proposal = models.URLField(blank=True, null=True)
    daily_scrum = models.ForeignKey(DailyScrum, on_delete=models.CASCADE)
    product_backlogs = models.ManyToManyField(ProductBacklog, blank=True, null=True)
    other = models.CharField(blank=True, null=True)
