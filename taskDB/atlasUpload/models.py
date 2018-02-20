from django.db import models

class Task(models.Model):
	aufgabenname = models.CharField(max_length=255)
	lehrer = models.CharField(max_length=255)
	uploadDate = models.DateTimeField('Date published')
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	thumbnailPath = models.CharField(max_length=255)
	deleted = False
	def __str__(self):
		return self.aufgabenname
	class Meta:
		verbose_name_plural = "Aufgaben"
