# bootcamp_lessons/forms.py

from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson # Tell the form which model to use
        fields = ['title', 'description', 'order'] # Which fields from the model to include in the form
        widgets = {
            'description': forms.Textarea(attrs={'rows':5}) # Make description a larger text area
        }