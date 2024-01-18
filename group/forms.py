from django import forms
from .models import group

# รับจำนวนที่ต้องการสร้างกลุ่ม
class GroupCreationForm(forms.ModelForm):
     number_of_groups = forms.IntegerField(min_value=1)
     class Meta:
        model = group
        fields = ['subject_name', 'number_of_groups']

# ผู้ใช้สามารถเพิ่มกลุ่ม
class GroupForm(forms.ModelForm):
    class Meta:
        model = group
        fields = ['subject_name']
