from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255, unique=True, verbose_name='Name des Fachs')

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = "Fach"
        verbose_name_plural = "Fächer"


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255, verbose_name='Aufgabe')
    task_description = models.CharField(max_length=1000, blank=True, verbose_name='Beschreibung')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Hochgeladen')
    last_changed_at = models.DateTimeField(auto_now=True, verbose_name='Zuletzt geändert')
    document = models.FileField(upload_to='Tasks/%Y/%m', verbose_name='Dateipfad')
    teacher = models.ForeignKey(User, related_name="teacher", on_delete=models.CASCADE, verbose_name='Lehrer')
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True, verbose_name='Fach')
    stage = models.IntegerField(validators=[MaxValueValidator(13), MinValueValidator(1)], verbose_name='Klassenstufe')

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = "Aufgabe"
        verbose_name_plural = "Aufgaben"
