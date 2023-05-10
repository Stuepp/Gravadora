from django import forms
from .models import Musica, Musico, Banda, Own, Participa, Instrumento, Disco, Produtor

class AddMusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ('titulo','autores','file','image')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            #'autores': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'autores': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'type': 'file', 'required': True}),
            'image': forms.FileInput(attrs={'type': 'file', 'required': True}),
        }

class AddMusicoForm(forms.ModelForm): # preciso fazer um sistema que insere um id automatico?
    class Meta: # lembrando que Musico é filho de Own
        model = Musico
        fields = ('endereco','telefone','nome')

        widgets = { # musico tem os instrumentos que ele toca
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }

class AddBandaForm(forms.ModelForm): # preciso fazer um sistema que insere um id automatico?
    class Meta: # lembrando que Banda é filha de Own
        model = Banda
        fields = ('nome',)

        widgets = { # a banda tem os musicos que estão nela
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
        fields = ('titulo','formato','data','fk_musico','fk_banda')

        widgets = { # pelo menos o musico ou a banda tem que ser escolhido
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'formato': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'data': forms.DateTimeInput(attrs={'type': 'date', 'required': True}), # tyoe data?
            'musico': forms.TextInput(attrs={'class': 'form-control'}), # alterar para autocomplete ou select box?
            'banda': forms.TextInput(attrs={'class': 'form-control'}), # alterar para autocomplete ou select box?
        }

class addProdutorForm(forms.ModelForm):
    class Meta:
        model = Produtor
        fields = ('nome',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }