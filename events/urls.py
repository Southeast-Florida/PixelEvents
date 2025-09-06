from django.urls import path
from .views import create_event, event_created, participant_dashboard

urlpatterns = [
    path('create/', create_event, name='create_event'),
    path('created/', event_created, name='event_created'),
    path('participant/dashboard/', participant_dashboard, name='participant_dashboard'),
]
