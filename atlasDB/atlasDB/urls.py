from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('changelog/', include('changelog.urls')),
    path('', include('atlas.urls')),
]
