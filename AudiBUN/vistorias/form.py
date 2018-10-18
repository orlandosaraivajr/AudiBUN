from django import forms
from django.forms import ModelForm

from AudiBUN.vistorias.models import VistoriaModel

class VistoriaForm(ModelForm):
    class Meta:
        model = VistoriaModel
        fields = ('empresa', 'imagem', 'observacao')
        # exclude = ['created_at']
        labels = {
            'empresa': 'Empresa',
            'imagem': 'Foto',
            'observacao': 'Observação',
        }
        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }