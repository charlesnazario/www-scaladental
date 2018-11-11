from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ouroffice/', views.ouroffice, name='ouroffice'),
    path('contact/', views.contact, name='contact'),
]