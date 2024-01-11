from django.db import models
from teacher.models import *

# Create your models here.
class student (models.Model):
    student_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.ForeignKey(teacher, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.student_id)