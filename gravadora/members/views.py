from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.views.generic.edit import FormView
from .forms import AddForm
from .models import Musico, Own, Musica, Participa
# Create your views here.

class ShowPlayListView(View):
    template_name = 'index.htm'
    context = {
        'musico': Musico.objects.get(id=1),
        'musica' : Musica.objects.get(id=5),
        'musicas' : Musica.objects.all().values() # selecionar futuramente apenas musicas da playlist/disco
    }
    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(self.context, request))

class SaveSongForm(FormView): # alterar para conseguir fazer upload já com a ligação entre musica participa e own
    template_name = 'add.htm'
    form_class = AddForm
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ShowSaveSong(View):
    template_name = 'aud.htm'
    musicos = Musico.objects.all().values()
    context = {
        'musicos' : musicos,
    }

    def get(self, request, *args, **kwargs):      
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(self.context, request))

    def post(self, request, *args, **kwargs):
        #if request.method == 'POST':
        form = self.form_class(request.POST)
        if form.is_valid():
            audio = request.FILES['audio']
            image_r = request.FILES['image']
            titulo_r = request.POST['titulo']
            autores_r = request.POST['autores']
            musica = Musica.objects.create(
                titulo= titulo_r,
                autores = autores_r,
                file=audio,
                image = image_r
            )
            musica.save()
            audio_path = musica.file.path

            autor_r = request.POST['aut']
            autor = Musico.objects.get(nome=autor_r)
            own = Own.objects.create(
                fk_musico = autor
            )
            own.save()

            particpa = Participa.objects.create(
                fk_own = own,
                fk_musica = musica
            )

            template = loader.get_template(self.template_name)
            musicos = Musico.objects.all().values()
            context = {
                'audio_path':audio_path,
                'musicos': musicos,
                }
            return HttpResponse(template.render(context, request))
            #return render(request, self.template_name, {'audio_path':audio_path, 'musicos':Musico.objects.all().values()})
        #return render(request, 'aud.htm')