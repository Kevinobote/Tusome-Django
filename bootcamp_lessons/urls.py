# bootcamp_lessons/urls.py

from django.urls import path
from .import views # Import the views from the current app

urlpatterns = [
    path('', views.home, name='home'), # When someone visits /, call the home view
    path('intro/', views.intro, name='intro'), # When someone visits /intro/, call the intro view
    path('get-started/', views.get_started, name='get_started'), # When someone visits /get-started/, call the get_started view
]