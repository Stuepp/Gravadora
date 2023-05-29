from django.urls import path
from . import views

urlpatterns = [
    path('menu/teste/', views.teste, name='teste'),
    #path('', views.ShowPlayListView.as_view(),name='index'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('addMusico/', views.SaveMusicoForm.as_view(), name='addMusico'),
    path('addMusica/', views.SaveMusicaForm.as_view(), name='addMusica'),
    path('addBanda/', views.SaveBandaForm.as_view(), name='addBanda'),
    path('addInstrumento/', views.SaveInstrumentoForm.as_view(), name='addInstrumento'),
    path('addDisco/', views.SaveDiscoForm.as_view(), name='addDisco'),
    path('addProdutor/', views.SaveProdutorForm.as_view(), name='addProdutor'),
]