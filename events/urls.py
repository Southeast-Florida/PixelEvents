from django.urls import path
from .views import create_event, event_created  # ← импортируем новое представление

urlpatterns = [
    path('create/', create_event, name='create_event'),
    path('created/', event_created, name='event_created'),  # ← новый маршрут
]
