from django.urls import path
from . import views
from members.views import ShowPlayListView

urlpatterns = [
    path('', ShowPlayListView.as_view(),name='index'),
    path('audio/',views.Musica_save, name='members'),
]