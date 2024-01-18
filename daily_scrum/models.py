from django.contrib.auth.models import User
from django.db import models


class DailyScrum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey('group.group', on_delete=models.CASCADE)
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
    other_description = models.TextField(blank=True, null=True,)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.date.strftime('%Y-%m-%d')
