from django.db import models

class Task(models.Model):
	aufgabenname = models.CharField(max_length=255)
	lehrer = models.CharField(max_length=255)
	uploaddate = models.DateTimeField('Hochgeladen am', auto_now_add=True)
	docfile = models.FileField(upload_to='tasks/%Y/%m')
	thumbnailPath = models.CharField(max_length=255)
	deleted = False
	def __str__(self):
		return self.aufgabenname
	class Meta:
		verbose_name_plural = "Aufgaben"