from django.db import models

# Create your models here.

class TodoItem(models.Model);
    title = models.CharField(max_length=255)
    description = modles.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated-at = models.DateTimeField(auto_now=True)

    def __str__(self);
        return self.title