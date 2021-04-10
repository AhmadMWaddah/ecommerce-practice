from django.urls import path
from page import views


urlpatterns = [
    path('about', views.about, name='about'),
    path('not_found', views.not_found, name='not_found'),
    path('showcases', views.showcases, name='showcases'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('privacy', views.privacy, name='privacy'),
    path('refund', views.refund, name='refund'),
    path('terms', views.terms, name='terms'),
    path('shipping', views.shipping, name='shipping'),
]