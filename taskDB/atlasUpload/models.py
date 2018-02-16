from django.db import models

class Task(models.Model):
	aufgabenname = models.CharField(max_length=255)
	lehrer = models.CharField(max_length=255)
	uploadDate = models.DateTimeField('Date published')
	dataPath = models.CharField(max_length=255)
	thumbnailPath = models.CharField(max_length=255)
	deleted = False
	def __str__(self):
		return self.aufgabenname
	class Meta:
		verbose_name_plural = "Aufgaben"
