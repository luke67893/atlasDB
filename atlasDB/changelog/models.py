from django.db import models
from datetime import datetime

class ChangelogPost(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	date = models.DateTimeField('Date published', default=datetime.now)
	author = models.TextField()
	# This is just for showing the title in the admin interface
	def __str__(self):
		return self.title
	# Showing right category in admin interface
	class Meta:
		verbose_name_plural = "Changelog Posts"