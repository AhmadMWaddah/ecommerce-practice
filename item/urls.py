from django.urls import path
from item import views


urlpatterns = [
    path('', views.items, name='items'),
    path('<str:itm_sku>', views.item, name='item'),
    path('search', views.item_search, name='item_search'),
]