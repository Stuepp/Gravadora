from django import forms
from .models import Musica, Musico, Banda, Own, Participa

class AddForm(forms.ModelForm):
    
    class Meta:
        model = Musica
        fields = ('titulo','autores','file','image')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'type': 'file'}),
            'image': forms.FileInput(attrs={'type': 'file'}),
        }