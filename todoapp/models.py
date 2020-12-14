from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=200)
    timestamp = models.DateTimeField(null=True)


    def __str__(self):
        return self.text