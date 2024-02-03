from django.contrib import admin

from projectall.models import ProjectDetail, ProjectGroup

# Register your models here.
#class ProjectAllAdmin(admin.ModelAdmin):
   # list_display = ['group_id']

admin.site.register(ProjectGroup)
admin.site.register(ProjectDetail)