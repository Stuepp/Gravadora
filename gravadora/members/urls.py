from django.urls import path
from . import views
from members.views import ShowPlayListView, ShowSaveSong, SaveSongForm

urlpatterns = [
    path('', ShowPlayListView.as_view(),name='index'),
    path('audio/',ShowSaveSong.as_view(), name='aud'),
    path('add/', SaveSongForm.as_view(), name='add'),
]