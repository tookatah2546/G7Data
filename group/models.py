from django.db import models


# Create your models here.
    
class group (models.Model):
    group_id = models.CharField(max_length=50)
    subject_name = models.CharField(default='project',max_length=50)
    

    def __str__(self):
        return str(self.group_id)
    
class teacher (models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # group = models.ForeignKey(group, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.username)
