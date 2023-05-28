from django.urls import path
from . import views
from members.views import ShowPlayListView, SaveMusicoForm, SaveBandaForm, SaveInstrumentoForm, SaveDiscoForm, SaveProdutorForm, SaveMusicaForm

urlpatterns = [
    path('', ShowPlayListView.as_view(),name='index'),
    path('addMusico/', SaveMusicoForm.as_view(), name='addMusico'),
    path('addMusica/', SaveMusicaForm.as_view(), name='addMusica'),
    path('addBanda/', SaveBandaForm.as_view(), name='addBanda'),
    path('addInstrumento/', SaveInstrumentoForm.as_view(), name='addInstrumento'),
    path('addDisco/', SaveDiscoForm.as_view(), name='addDisco'),
    path('addProdutor/', SaveProdutorForm.as_view(), name='addProdutor'),
]

