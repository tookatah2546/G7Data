from django.db import models
from django.contrib.auth.models import User
from backend import settings

#กลุ่มที่อาจารย์สร้าง
class ProjectGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    project_count = models.PositiveIntegerField(default=0)
    members = models.ManyToManyField('Student', related_name='project_groups', blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups', default=settings.DEFAULT_TEACHER_ID)

#นิสิต
class Student(models.Model):
    student_id = models.CharField(max_length=8, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group_student = models.ForeignKey(ProjectGroup, on_delete=models.CASCADE, related_name='students')
    

#daily scrum(form)

#backlog
class ProductBacklog(models.Model):
    group_Backlog = models.ForeignKey(ProjectGroup, on_delete=models.CASCADE)
    backlog_id = models.CharField(max_length=255)
    backlog_name = models.CharField(max_length=255)
    date_to_done = models.DateField()
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )
    # status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='todo')
    date_done = models.DateField()
    IM_CHOICES = (
        ('low', 'ต่ำ'),
        ('mid', 'ปานกลาง'),
        ('hight', 'มาก'),
    )
    # im = models.CharField(max_length=3, choices=IM_CHOICES, default='low')
    # task = models.ForeignKey(Task, on_delete=models.CASCADE)

#task
class Task(models.Model):
    product_backlog = models.ForeignKey(ProductBacklog, on_delete=models.CASCADE)
    task_id = models.CharField(max_length=255)
    task_name = models.CharField(max_length=255)
    '''STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )'''
    # status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='todo')

#รายละเอียดกลุ่ม
class ProjectDetail(models.Model):
    project_name = models.CharField(max_length=255)
    trello_link = models.URLField(blank=True)
    figma_link = models.URLField(blank=True)
    # proposal = models.URLField(blank=True)
    # daily_scrum = models.ForeignKey(DailyScrum, on_delete=models.CASCADE)
    product_backlogs = models.ManyToManyField(ProductBacklog, blank=True)
    # other = models.CharField(blank=True)

#วิชา
class Subject(models.Model):
    name = models.CharField(max_length=255)


# ที่คอมเมคือยังไม่ได้migrate