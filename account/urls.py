from django.urls import path
from account import views

urlpatterns = [
	path('register', views.account_register, name='register'),
	path('login', views.account_login, name='login'),
	path('logout', views.account_logout, name='logout'),
]
