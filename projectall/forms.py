
from django import forms

class ProjectGroupForm(forms.Form):
    subject = forms.CharField(max_length=255)  # แก้นี้
    project_count = forms.IntegerField()

