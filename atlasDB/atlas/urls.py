from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.upload),
	path('upload/', views.upload, name='upload'),
	path('upload/success/', views.success, name='success'),
	path('upload/errorx1/', views.errorx1, name='errorx1'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('aufgabe/<int:id>/', views.aufgabe, name='aufgabe'),
	path('download/<int:id>/', views.download, name='download'),
]