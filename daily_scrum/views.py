# views.py
from django.shortcuts import render, redirect
from .models import DailyScrum
from .forms import DailyScrumForm
from django.contrib.auth.models import User

def create_daily_scrum(request):
    if request.method == 'POST':
        form = DailyScrumForm(request.POST)
        if form.is_valid():
            daily_scrum = form.save(commit=False)
            daily_scrum.user = request.user  # assuming you are using the built-in User model
            daily_scrum.save()
            print(daily_scrum)
            return redirect('daily_scrum_list')  # Redirect to the list view
    else:
        form = DailyScrumForm()

    return render(request, 'create_daily_scrum.html', {'form': form})
    

def daily_scrum_list(request):
    # Assuming you want to display all daily scrum entries
    daily_scrum_entries = DailyScrum.objects.all()
    return render(request, 'daily_scrum_list.html', {'daily_scrum_entries': daily_scrum_entries})

