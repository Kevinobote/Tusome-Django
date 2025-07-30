# bootcamp_lessons/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Lesson
from .forms import LessonForm
from .forms import LessonForm
# from django.http import HttpResponse # No longer needed for these views

# Home page view
def home(request):
    return render(request, 'bootcamp_lessons/home.html')

# Intro page view
def intro(request):
    return render(request, 'bootcamp_lessons/intro.html')

# Get Started page view
def get_started(request):
    return render(request, 'bootcamp_lessons/get_started.html')

# Lesson list view
def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'bootcamp_lessons/lesson_list.html', {'lessons': lessons})

# Lesson detail view
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'bootcamp_lessons/lesson_detail.html', {'lesson': lesson})

# Lesson create view
def lesson_create(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson created successfully!')
            return redirect('lesson_list')
    else:
        form = LessonForm()
    return render(request, 'bootcamp_lessons/lesson_form.html', {'form': form, 'form_type': 'Create'})

# View to update an existing lesson
def lesson_update(request, pk):
        lesson = get_object_or_404(Lesson, pk=pk) # Get the lesson to update
        if request.method == 'POST':
            form = LessonForm(request.POST, instance=lesson) # Populate form with submitted data AND existing lesson instance
            if form.is_valid():
                form.save() # Save the updated lesson
                messages.success(request, 'Lesson updated successfully!')
                return redirect('lesson_detail', pk=lesson.pk) # Go back to the lesson's detail page
        else:
            form = LessonForm(instance=lesson) # Populate form with existing lesson data for GET requests
        return render(request, 'bootcamp_lessons/lesson_form.html', {'form': form, 'form_type': 'Update'})

# View to delete a lesson
def lesson_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk) # Get the lesson to delete
    if request.method == 'POST':
        lesson.delete() # Delete the lesson from the database
        messages.info(request, 'Lesson deleted successfully!')
        return redirect('lesson_list') # Go back to the lesson list
    return render(request, 'bootcamp_lessons/lesson_confirm_delete.html', {'lesson': lesson})
