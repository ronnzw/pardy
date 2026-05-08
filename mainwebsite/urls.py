from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .sitemaps import StaticViewSitemap

sitemaps = {'static': StaticViewSitemap}


urlpatterns = [
    path('',views.home, name='home'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', views.robots_txt),
]
