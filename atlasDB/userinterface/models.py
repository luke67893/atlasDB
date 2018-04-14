from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Subject(models.Model):
    subject_name = models.CharField(max_length=25)

class Stage(models.Model):
    stage_level = models.IntegerField(validators=[MaxValueValidator(13),MinValueValidator(1)]
     )

class Task(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    last_changed_at = models.DateTimeField(auto_now=True)
    task_name = models.CharField(max_length=255)
    document = models.FileField(upload_to='Tasks/%Y/%m')
    teacher = models.ForeignKey(User, related_name="teacher", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
