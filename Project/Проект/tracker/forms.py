from django import forms
from datetime import datetime
from .models import Habit

class HabitCreate(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'frequency', 'description']