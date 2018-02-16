from django.contrib import admin

# Showing the changelog post tool in the admin interface
from .models import ChangelogPost
admin.site.register(ChangelogPost)