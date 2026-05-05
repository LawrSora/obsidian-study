from django.contrib import admin
from .models import Habit
from .models import HabitEntry
from .models import User

# Register your models here.

admin.site.register(Habit)
admin.site.register(HabitEntry)