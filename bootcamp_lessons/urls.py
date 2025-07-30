# bootcamp_lessons/urls.py

from django.urls import path
from . import views # Import the views from the current app

urlpatterns = [
    path('', views.home, name='home'),
    path('intro/', views.intro, name='intro'),
    path('get-started/', views.get_started, name='get_started'),
    path('lessons/', views.lesson_list, name='lesson_list'), # List all lessons
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'), # View a single lesson
    path('lessons/new/', views.lesson_create, name='lesson_create'), # Create a new lesson
    path('lessons/<int:pk>/edit/', views.lesson_update, name='lesson_update'), # Edit an existing lesson
    path('lessons/<int:pk>/delete/', views.lesson_delete, name='lesson_delete'), # Delete a lesson
]