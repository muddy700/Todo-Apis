from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title