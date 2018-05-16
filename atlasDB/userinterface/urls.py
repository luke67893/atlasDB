from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url

from . import views

urlpatterns = [
	path('login/', LoginView.as_view(template_name="userinterface/login_form.html"), name="user_login"),
	path('logout/', LogoutView.as_view(), name="user_logout"),
	path('home/', views.user_home, name="user_home"),
	path('my_tasks/', views.my_tasks, name="my_tasks"),
	path('upload/', views.upload, name="upload"),
	path('stages/', views.stages, name="stages"),
	path('stage_<int:id>/', views.stage, name="stage"),
	path('task/<int:id>/', views.details, name="task"),
	path('download/<path:path>', views.download, name="download"),
	path('', views.welcome, name="welcome"),
]
