from django.db import models
from group.models import *

# Create your models here.
class student (models.Model):
    student_id = models.CharField(max_length=8)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.ForeignKey(group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student_id)
    
class group (models.Model):
    group_name = models.CharField(max_length=100)
    trello_link = models.URLField()
    figma_link = models.URLField()
    other = models.CharField(max_length=500)

    def __str__(self):
        return str(self.group_id)
   