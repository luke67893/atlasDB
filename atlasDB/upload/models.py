from django.db import models
from datetime import datetime

class Aufgabe(models.Model):
	titel = models.CharField(max_length=255)
	lehrer = models.CharField(max_length=255)
	datum = models.DateTimeField('Hochgeladen am', default=datetime.now)
	datensatz = models.FileField(upload_to='Aufgaben/%Y/%m')
	def __str__(self):
		return self.titel
	class Meta:
		verbose_name_plural = "Aufgaben"