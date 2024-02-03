from rest_framework import serializers
from .models import ProjectGroup

class ProjectGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGroup
        fields = ('group_id','subject','project_count','teacher',)