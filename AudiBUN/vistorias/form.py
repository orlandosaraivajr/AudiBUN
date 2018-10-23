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
        error_messages = {
            'empresa': {
                'required': ("Selecione a empresa fiscalizada."),
            },
            'imagem': {
                'required': ("Selecione uma foto da vistoria."),
            }
        }

    def read_only(self, read_only=True):
        ''' Set fields with attribute readonly'''
        fields = list(self.fields)
        if read_only:
            for field in fields:
                self.fields[field].widget.attrs['readonly'] = True
        else:
            for field in fields:
                self.fields[field].widget.attrs['readonly'] = False

    def clean_observacao(self):
        return self.cleaned_data['observacao'].upper()
