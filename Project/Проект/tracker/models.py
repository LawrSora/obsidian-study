from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import FloatField, BooleanField, CharField, UniqueConstraint
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    frequency = models.IntegerField()
    last_date = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name.title()}"

class HabitEntry(models.Model):
    entry_date = models.DateField(auto_now_add=True)
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE)
    done = models.BooleanField()