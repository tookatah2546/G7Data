import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _ 


#   Bad smell --x  Extract class  x--
#กลุ่มที่อาจารย์สร้าง
class ProjectGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    project_count = models.PositiveIntegerField(default=0)
    members = models.ManyToManyField('Student', related_name='project_groups', blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups', default=1)
    
class AppRole(models.TextChoices) :
     STUDENT = "STD", _("Student")
     TEACHER = "TCH", _("Teacher")

class AppUser(AbstractUser) :
     role = models.CharField(
          max_length=255,
          choices=AppRole.choices,
     )
     id_student = models.CharField(max_length=8,default='')
     first_name = models.CharField(max_length=255, default='')
     last_name =  models.CharField(max_length=255, default='')

class Subject(models.Model):
     #group_id = models.AutoField(primary_key=True, null=False,blank=True)
     teacher = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True,blank=True)
     subject_name = models.CharField(max_length=255, default='')
     amount = models.PositiveBigIntegerField(default=0)

     '''def __str__(self):
          return str(self.subject_name)
'''
class Project(models.Model) :
     subject = models.ForeignKey(Subject , on_delete=models.SET_NULL, null=True,blank=True)
     users = models.ManyToManyField(AppUser)
     project_name = models.CharField(max_length=255, default='')
     trello_link = models.URLField(null=True,blank=True)
     figma_link = models.URLField(null=True,blank=True)

#นิสิต
class Student(models.Model):
    student_id = models.CharField(max_length=8, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group_student = models.ForeignKey(ProjectGroup, on_delete=models.CASCADE, related_name='students')
    student =  models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True,blank=True)
    group = models.ForeignKey(Subject , on_delete=models.SET_NULL, null=True,blank=True)


#daily scrum(form)
"""class DailyScrum(models.Model):
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
    # note_other = models.TextField(max_length=255)
    """

#backlog
class ProductBacklog(models.Model):
    group_Backlog = models.ForeignKey(ProjectGroup, on_delete=models.CASCADE)
    backlog_id = models.CharField(max_length=255)
    backlog_name = models.CharField(max_length=255)
    date_to_done = models.DateField()
    '''STATUS_CHOICES = (
class ProductBacklogs(models.Model):
     product = models.ForeignKey(Project , on_delete=models.SET_NULL, null=True,blank=True)
     #name_backlog = models.CharField(max_length=255,default='')
     date_to_do = models.DateField(default=datetime.date.today)
     STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )'''
    # status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='todo')
    date_done = models.DateField()
    '''IM_CHOICES = (
     )
     status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='todo')
     date_done = models.DateField(default=datetime.date.today)
     IM_CHOICES = (
        ('low', 'ต่ำ'),
        ('mid', 'ปานกลาง'),
        ('hight', 'มาก'),
    )'''
    # im = models.CharField(max_length=3, choices=IM_CHOICES, default='low')
    # task = models.ForeignKey(Task, on_delete=models.CASCADE)
    # important = models.CharField(max_length=5, choices=IM_CHOICES, default='low')

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
class  DailyScrum(models.Model) :
     student =  models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True,blank=True)
     date = models.DateField(auto_now_add = True)
     yesterday = models.CharField(max_length=1000)
     today = models.CharField(max_length=1000)
     problem = models.CharField(max_length=1000)
     NOTE_CHOICES = [
     ('work', 'วันนี่ทำงาน'),
     ('sick', 'ป่วย'),
     ('busy', 'ติดธุระ'),
     ('pass', 'ตกลงกันว่าวันนี้ไม่ทำงาน'),
     ]
     note = models.CharField(max_length=4, choices=NOTE_CHOICES)
     others = models.TextField(max_length=255)

class Tasks(models.Model):
     # product_backlogs = models.ForeignKey(ProductBacklogs, on_delete=models.CASCADE)
     task_id = models.CharField(max_length=255)
     task_name = models.CharField(max_length=255)
     STATUS_CHOICES = (
          ('todo', 'To Do'),
          ('doing', 'Doing'),
          ('done', 'Done'),
     )
     status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='todo')

#วิชา
class Subject(models.Model):
    name = models.CharField(max_length=255)