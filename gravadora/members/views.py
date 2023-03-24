from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Musico, Own, Musica
# Create your views here.
def members(request):
    musicos = Musico.objects.all().values() #otimizar na entrega final
    musicas = Musica.objects.all().values()
    context = {
        'musicos': musicos,
        'musicas':musicas
    }
    template = loader.get_template('index.htm')
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

 
        