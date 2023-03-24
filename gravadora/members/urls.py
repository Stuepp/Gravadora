from django.urls import path
from . import views

urlpatterns = [
    path('',views.members, name='members'),
    path('audio/',views.Musica_save, name='members'),
]