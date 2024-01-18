from django.shortcuts import render, redirect
from .models import group
from .forms import GroupForm, GroupCreationForm
from django.contrib.auth.models import User

def group_list(request):
    groups = group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

def create_group(request):
    form = GroupForm(request.POST or None)
    group_creation_form = GroupCreationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('group_list')

    if request.method == 'POST' and group_creation_form.is_valid():
        number_of_groups = group_creation_form.cleaned_data['number_of_groups']
        for _ in range(number_of_groups):
            # Create groups here and save to the database
            group_instance = group.objects.create(subject_name=group_creation_form.cleaned_data['subject_name'])
            group_instance.members.add(User.objects.first())        
            return redirect('group_list')

    return render(request, 'create_group.html', {'form': form, 'group_creation_form': group_creation_form})

# def create_groups_auto(request):
    
    return render(request, 'create_groups.html', {})
