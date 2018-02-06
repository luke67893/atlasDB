from django.db import models

# changelog post

class ChangelogPost(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	date = models.DateTimeField('date published')
	author = models.TextField()
	# This is just for showing the title in the admin interface
	def __str__(self):
		return self.title