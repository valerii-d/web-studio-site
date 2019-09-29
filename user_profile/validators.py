from django.forms import ValidationError
from django.utils import timezone

def validate_deadline(value):
    if value<=timezone.now():
        raise ValidationError("The date cannot be in the past!")
    return value