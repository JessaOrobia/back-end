from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=255, default="No title")  
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
