from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventForm

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return render(request, 'events/event_created.html', {'event': event})
    else:
        form = EventForm()
    return render(request, 'events/main2.html', {'form': form})

def event_created(request):
    return render(request, 'events/event_created.html')

@login_required
def participant_dashboard(request):
    return render(request, 'events/participant_dashboard.html')
