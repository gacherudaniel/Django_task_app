from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)#Task title
    description = models.TextField(blank = True)#Optional description
    completed = models.BooleanField(default=False)#Task status
    created_at = models.DateTimeField(auto_now_add=True)#Task creation date
    updated_at = models.DateTimeField(auto_now=True)#Task creation date
    

    def __str__(self):
        return self.title