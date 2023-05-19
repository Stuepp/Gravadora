from django import forms
from django.db.models.base import Model
from .models import Musica, Musico, Banda, Instrumento, Disco, Produtor

class CustomMusicaMusicoChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, musico):
        return "%s" % musico.nome
class CustomMusicaBandaChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, banda):
        return "%s" % banda.nome
class CustomMusicaDiscoChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, disco):
        return "%s" % disco.titulo

class AddMusicaForm(forms.ModelForm): # tentar reduzir MusicaMusico e MusicaBanda para MusicaMusicoBanda
    class Meta:
        model = Musica
        fields = ('titulo','autores','file','image','participa_Musico','participa_Banda', 'aparece')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'autores': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'file': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'type': 'file', 'class': 'form-control'}),
        }
    participa_Musico = CustomMusicaMusicoChoiceField(
        queryset=Musico.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    participa_Banda = CustomMusicaBandaChoiceField(
        queryset=Banda.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    aparece = CustomMusicaDiscoChoiceField(
        queryset = Disco.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class AddMusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ('endereco','telefone','nome', 'esta','toca')

        widgets = {
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
    esta = forms.ModelMultipleChoiceField(
        queryset=Banda.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    toca = forms.ModelMultipleChoiceField(
        queryset=Instrumento.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class AddBandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ('nome',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }

class AddInstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ('nome',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }

class AddDiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ('titulo','formato','data','disco_musico','disco_banda')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'formato': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'data': forms.DateTimeInput(attrs={'type': 'date', 'required': True}), # tyoe data?
        }
    disco_musico = CustomMusicaMusicoChoiceField(  # tentar reduzir MusicaMusico e MusicaBanda para MusicaMusicoBanda
        queryset=Musico.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    disco_banda = CustomMusicaBandaChoiceField(
        queryset=Banda.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class addProdutorForm(forms.ModelForm):
    class Meta:
        model = Produtor
        fields = ('nome',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }