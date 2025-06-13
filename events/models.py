from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cover = models.FileField(upload_to='covers/', blank=True, null=True)
    max_participants = models.PositiveIntegerField()

    def __str__(self):
        return self.title
