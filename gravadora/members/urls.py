from django.urls import path
from . import views

urlpatterns = [
    path('', views.Menu.as_view(), name='menu'),
    #path('', views.ShowPlayListView.as_view(),name='index'),
    path('disco/', views.disco, name='disco'),
    path('disco2/<int:musica>/<int:disco>', views.disco, name = 'disco2'),
    path('addMusico/', views.SaveMusicoForm.as_view(), name='addMusico'),
    path('addMusica/', views.SaveMusicaForm.as_view(), name='addMusica'),
    path('addBanda/', views.SaveBandaForm.as_view(), name='addBanda'),
    path('addInstrumento/', views.SaveInstrumentoForm.as_view(), name='addInstrumento'),
    path('addDisco/', views.SaveDiscoForm.as_view(), name='addDisco'),
    path('addProdutor/', views.SaveProdutorForm.as_view(), name='addProdutor'),
]