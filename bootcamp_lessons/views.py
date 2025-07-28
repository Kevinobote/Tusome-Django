# bootcamp_lessons/views.py
from django.shortcuts import render
from django.http import HttpResponse # We will use this for simple text responses first

# Home page view
def home(request):
    return HttpResponse("<h1>Welcome to Django Bootcamp Home!</h1><p>This is the main page.</p>")

# Intro page view
def intro(request):
    return HttpResponse("<h1>Django Intro</h1><p>Learn what Django is all about!</p>")

# Get started page view
def get_started(request):
    return HttpResponse("<h1>Get Started with Django</h1><p>Follow these steps to begin your journey!.</p>")