from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True)
    is_done = models.BooleanField(default=False)
    event_date = models.DateField()

    def __str__(self):
        return f'{self.user}-{self.title}-{self.event_date}'