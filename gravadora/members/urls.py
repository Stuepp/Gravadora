from django.urls import path
from . import views
from members.views import ShowPlayListView, SaveMusicoForm, SaveBandaForm, SaveInstrumentoForm, SaveDiscoForm, SaveProdutorForm, SaveMusicaForm

urlpatterns = [
    path('', ShowPlayListView.as_view(),name='index'),
    path('addMusico/', SaveMusicoForm.as_view(), name='add'),
    path('addMusica/', SaveMusicaForm.as_view(), name='add'),
    path('addBanda/', SaveBandaForm.as_view(), name='add'),
    path('addInstrumento/', SaveInstrumentoForm.as_view(), name='add'),
    path('addDisco/', SaveDiscoForm.as_view(), name='add'),
    path('addProdutor/', SaveProdutorForm.as_view(), name='add'),
]