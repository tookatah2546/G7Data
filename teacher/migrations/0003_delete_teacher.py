# Generated by Django 5.0.1 on 2024-01-13 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_group'),
        ('teacher', '0002_remove_teacher_group_remove_teacher_subject_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='teacher',
        ),
    ]