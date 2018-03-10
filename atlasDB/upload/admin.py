from django.contrib import admin

from .models import Aufgabe
admin.site.register(Aufgabe)
from .models import Tag
admin.site.register(Tag)