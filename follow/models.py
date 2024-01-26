from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=500)

class ProjectGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    project_count = models.PositiveIntegerField(default=0)