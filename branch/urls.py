from django.urls import path
from branch import views

urlpatterns = [
	path('', views.branch, name='branches')
]
