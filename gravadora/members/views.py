from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.views import View
from .models import Musico, Own, Musica
# Create your views here.

class ShowPlayListView(View):
    """
    template_name = 'index.htm'    
    context = {
        'musico_atual': Musico.objects.get(id=1),
        'musica_atual' : Musica.objects.get(id=4),
        'musicas' : Musica.objects.all().values() # selecionar futuramente apenas musicas da playlist
    }
    """
    def get(self, request, *args, **kwargs):
        template = loader.get_template('index.htm')
        context = {
            'musico': Musico.objects.get(id=1),
            'musica' : Musica.objects.get(id=4),
            'musicas' : Musica.objects.all().values() # selecionar futuramente apenas musicas da playlist
        }
        return HttpResponse(template.render(context, request))


def Musica_save(request): # está funcionando! testar agora imagem e audio
    if request.method == 'POST':
        audio = request.FILES['audio']
        image_r = request.FILES['image']
        titulo_r = request.POST['titulo']
        autores_r = request.POST['autores']
        audio_file = Musica.objects.create(
            titulo= titulo_r,
            autores = autores_r,
            file=audio,
            image = image_r
        )
        audio_file.save()
        audio_path = audio_file.file.path
        return render(request, 'aud.htm', {'audio_path':audio_path})
    return render(request, 'aud.htm')

 
        