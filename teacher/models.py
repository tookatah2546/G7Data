from django.db import models
from django.contrib.auth.models import User


class teachers_user(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE),
    password = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_name)