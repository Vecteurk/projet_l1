from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name="contact"),
    path('inscription/', views.inscription, name="inscription"),
    path('apropos/', views.apropos, name="apropos"),
]