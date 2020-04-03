from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
# Create your models here.
# def text_exists(value):
#     todo_items=Todo.objects.all()
#     if value  in  todo_items:
#         raise ValidationError("you already enter the value")
#validators=[text_exists]
class Todo(models.Model):
    text=models.CharField(max_length=200,unique=True)
    added_date=models.DateTimeField(default=timezone.now()-timedelta(hours=6, minutes=30))

    def __str__(self):
        return self.text
