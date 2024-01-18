from django import forms
from project.models import Subject

class ProjectGroupForm(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    project_count = forms.IntegerField()
