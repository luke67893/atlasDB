from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	# path('', include('changelog.urls')),
    path('admin/', admin.site.urls),
    path('changelog/', include('changelog.urls')),
    path('upload/', include('atlasUpload.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
