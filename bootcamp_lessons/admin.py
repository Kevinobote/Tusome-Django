# bootcamp_lessons/admin.py

from django.contrib import admin
from .models import Lesson # Import your Lesson model

admin.site.register(Lesson) # Register the Lesson model with the admin site
