from django.db import models
from teacher.models import *

# Create your models here.
    
class group (models.Model):
    
    group_name = models.CharField(max_length=100)
    trello_link = models.URLField()
    figma_link = models.URLField()
    other = models.CharField(max_length=500)
   
    def __str__(self):
        return str(self.group_id)