
from django.urls import path
from barrow import views

urlpatterns = [
    path('', views.view_barrow, name='view_barrow'),
    path('add', views.add_to_barrow, name='add_to_barrow'),
    path('remove', views.remove_from_barrow, name='remove_from_barrow'),
    path('clear', views.clear_barrow, name='clear_barrow'),
]