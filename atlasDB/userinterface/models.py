from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    subject_name = models.CharField(max_lenght=50)

class Stage(models.Model):
    stage_level = models.IntegerField(validators=[MaxValueValidator(13), MinValueValidator(1)])

class Task(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    last_changed_at = models.DateTimeField(auto_now=True)
    task_name = models.CharField(max_lenght=255)
    document = models.FileField(upload_to='Tasks/%Y/%m')
    teacher = models.ForeignKey(User, related_name="teacher")
    subject = models.ForeignKey(Subject)
