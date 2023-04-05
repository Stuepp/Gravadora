from django import forms
from .models import Musica, Musico, Banda, Own, Participa, Instrumento, Disco, Produtor

class AddMusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ('titulo','autores','file','image')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'type': 'file'}),
            'image': forms.FileInput(attrs={'type': 'file'}),
        }

class AddMusicoForm(forms.ModelForm): # preciso fazer um sistema que insere um id automatico?
    class Meta:
        model = Musico
        fields = ('endereco','telefone','nome')

        widgets = {
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddBandaForm(forms.ModelForm): # preciso fazer um sistema que insere um id automatico?
    class Meta:
        model = Banda
        fields = ('nome',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddInstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ('nome',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddDiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ('titulo','formato','data','image','fk_musico','fk_banda')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'formato': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.FileInput(attrs={'type': 'data'}), # tyoe data?
            'image': forms.FileInput(attrs={'type': 'file'}),
            'musico': forms.TextInput(attrs={'class': 'form-control'}), # alterar para autocomplete ou select box?
            'banda': forms.TextInput(attrs={'class': 'form-control'}), # alterar para autocomplete ou select box?
        }

class addProdutorForm(forms.ModelForm):
    class Meta:
        model = Produtor
        fields = ('nome',)

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }