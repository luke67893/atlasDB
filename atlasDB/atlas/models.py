from django.db import models
from datetime import datetime

class Tag(models.Model):
	tagname = models.CharField(max_length=24)
	def __str__(self):
		return self.tagname
	class Meta:
		verbose_name_plural = "Tags"
		verbose_name = "Tag"

class Aufgabe(models.Model):
	titel = models.CharField(max_length=255)
	lehrer = models.CharField(max_length=255)
	datum = models.DateTimeField('Hochgeladen am', default=datetime.now)
	datensatz = models.FileField(upload_to='Aufgaben/%Y/%m')
	# tags = models.ManyToManyField(Tag, blank=True)
	def __str__(self):
		return self.titel
	class Meta:
		verbose_name_plural = "Aufgaben"
		verbose_name = "Aufgabe"
