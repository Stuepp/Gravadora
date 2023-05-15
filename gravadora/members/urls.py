from django.urls import path
from . import views
from members.views import ShowPlayListView, SaveSongForm, SaveMusicoForm, SaveBandaForm, SaveInstrumentoForm, SaveDiscoForm, SaveProdutorForm, SaveMusicaForm# ShowSaveSong

urlpatterns = [
    path('', ShowPlayListView.as_view(),name='index'),
    path('addMusica/', SaveSongForm.as_view(), name='add'),
    path('addMusico/', SaveMusicoForm.as_view(), name='add'),
    path('addMusica/', SaveMusicaForm.as_view(), name='add'),
    path('addBanda/', SaveBandaForm.as_view(), name='add'),
    path('addInstrumento/', SaveInstrumentoForm.as_view(), name='add'),
    path('addDisco/', SaveDiscoForm.as_view(), name='add'),
    path('addProdutor/', SaveProdutorForm.as_view(), name='add'),
]

#path('audio/',ShowSaveSong.as_view(), name='aud'),