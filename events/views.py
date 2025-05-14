from django.shortcuts import render, redirect
from .forms import EventForm

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()  # сохраняем объект и передаём его в шаблон
            return render(request, 'events/event_created.html', {'event': event})
    else:
        form = EventForm()
    return render(request, 'events/main2.html', {'form': form})

def event_created(request):
    # Если когда-то понадобится переход по прямой ссылке — можно обработать
    return render(request, 'events/event_created.html')
