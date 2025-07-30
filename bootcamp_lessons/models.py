# bootcamp_lessons/models.py

from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=200) # A short text field for the lesson title
    description = models.TextField() # Alonger text field for the lesson description
    order = models.IntegerField(unique=True) # An integer to define the order of lessons, must be unique
    is_published = models.BooleanField(default=False) # New field!
    
    def __str__(self):
        return self.title # This makes it easier to see the lesson title in the admin
    
    class Meta:
        ordering = ['order'] # Always sort lessons by their order number

