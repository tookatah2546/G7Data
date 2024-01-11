from django.db import models


# Create your models here.
class teacher (models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)
    group_id = models.IntegerField(max_length=50)

    def __str__(self):
        return str(self.username)
