from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
	path('login/', LoginView.as_view(template_name="userinterface/login_form.html"), name="user_login"),
	path('logout/', LogoutView.as_view(), name="user_logout"),
	path('main/', views.main, name="main"),
	path('', views.welcome, name="welcome_page"),
]
