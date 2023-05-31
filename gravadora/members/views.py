from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from django.views.generic.edit import FormView
from . import forms
from .models import Musico, Musica, Disco
from django.urls import reverse_lazy
# Create your views here.
"""
class ShowPlayListView(View):
    template_name = 'index.htm'
    #if Musico.objects.all()
    #d = Disco.objects.all().get(id=1)
    context = {
        'musico': Musico.objects.all().values(), #get(id=1), 
        'musica_atual' : Musica.objects.all().filter(aparece__id=d.id).first(), # música atual
        'disco': d,
        'musicas' : Musica.objects.all().filter(aparece__id=d.id)
    }
    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        d = Disco.objects.all().get(id=request.POST.get('disco', None))
        context = {
            'musico': Musico.objects.all().values(), #get(id=1), 
            'musica_atual' : Musica.objects.all().filter(aparece__id=d.id).first(), # música atual
            'disco': d,
            'musicas' : Musica.objects.all().filter(aparece__id=d.id)
        }
        return HttpResponse(template.render(context, request))
"""
def disco(request, musica, disco):
    template = loader.get_template('index.htm')
    d = Disco.objects.all().get(id=disco)#request.POST.get('disco', None))
    atual = musica
    anterior = atual - 1
    proxima = atual + 1
    if Musica.objects.all().filter(aparece__id=d.id):
        musica_atual = Musica.objects.all().filter(aparece__id=d.id)[atual]
    else:
        musica_atual = Musica.objects.all().filter(aparece__id=d.id)
    context = {
        'musico': Musico.objects.all().values(), #get(id=1), 
        'musica_atual' : musica_atual,
        'disco': d,
        'musicas' : Musica.objects.all().filter(aparece__id=d.id),
        'anterior': atual - 1,
        'atual': atual,
        'proxima': proxima,
        'anterior': anterior,
        'ultimo': len(Musica.objects.all().filter(aparece__id=d.id))-1,
    }
    return HttpResponse(template.render(context, request))

class Menu(View):
    template_name = 'menu.htm'
    context = {
        'discos': Disco.objects.all()
    }
    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(self.context,request))


class SaveMusicoForm(FormView):
    template_name = 'add.htm'
    form_class = forms.AddMusicoForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SaveMusicoForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Músico'
        return context

class SaveBandaForm(FormView):
    template_name = 'add.htm'
    form_class = forms.AddBandaForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SaveBandaForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Banda'
        return context

class SaveInstrumentoForm(FormView):
    template_name = 'add.htm'
    form_class = forms.AddInstrumentoForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SaveInstrumentoForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Instrumento'
        return context

class SaveDiscoForm(FormView):
    template_name = 'add.htm'
    form_class = forms.AddDiscoForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(SaveDiscoForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Disco'
        return context

class SaveProdutorForm(FormView):
    template_name = 'add.htm'
    form_class = forms.addProdutorForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(SaveProdutorForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Produtor'
        return context

class SaveMusicaForm(FormView): # multiple select box is not showing as expected
    template_name = 'add.htm'
    form_class = forms.AddMusicaForm
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs): # it's not showing title for some reason
        context = super(SaveMusicaForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Musica'
        return context