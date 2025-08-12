from django.db import models
from django.core.exceptions import ValidationError

def is_number(value):
    try:
        int(value) # Or float(value)
    except ValueError:
        raise ValidationError("Age must be blank or a valid number.")

# Create your models here.
class entry(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3, blank=True, validators=[is_number])
    title = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name