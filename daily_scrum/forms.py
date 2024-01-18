from django import forms
from .models import DailyScrum

class DailyScrumForm(forms.ModelForm):
    class Meta:
        model = DailyScrum
        fields = '__all__'