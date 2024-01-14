from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from group.models import group


class RegisterForm(UserCreationForm):
    # class Meta(UserCreationForm.Meta):
        รหัสนิสิต = forms.CharField()
        ชื่อจริง = forms.CharField()
        นามสกุล = forms.CharField()
        กลุ่ม = forms.ModelChoiceField(queryset=group.objects.all())
    