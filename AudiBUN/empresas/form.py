from django import forms
from django.forms import ModelForm

from AudiBUN.empresas.models import EmpresaModel, ATIVIDADE_CHOICES, DISTRITO_CHOICES


class EmpresaForm(ModelForm):
    class Meta:
        model = EmpresaModel
        exclude = ['created_at']

        labels = {
            'ref_cad': 'Referência Cadastral',
            'name': 'Nome',
            'categoria_atividade': 'Atividade',
            'atividade': 'Descrição da atividade',
            'endereco': 'Endereço',
            'quadra': 'Quadra',
            'lote': 'Lote',
            'categoria_distrito': 'Distrito',
            'email': 'E-mail',
            'phone': 'Fone',
            'responsavel': 'Responsável',
            'situacao': 'Situação',
            'observacao' : 'Observação',
        }
        widgets = {
            'ref_cad': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_atividade': forms.Select(choices=ATIVIDADE_CHOICES,attrs={'class': 'form-control'}),
            'atividade': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'quadra': forms.TextInput(attrs={'class': 'form-control'}),
            'lote': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_distrito': forms.Select(choices=DISTRITO_CHOICES, attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'situacao': forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        return  self.cleaned_data['name'].upper()

    def clean_quadra(self):
        return self.cleaned_data['quadra'].upper()

    def clean_atividade(self):
        return self.cleaned_data['atividade'].upper()

    def clean_endereco(self):
        return self.cleaned_data['endereco'].upper()

    def clean_lote(self):
        return self.cleaned_data['lote'].upper()

    def clean_responsavel(self):
        return self.cleaned_data['responsavel'].upper()

    def clean_situacao(self):
        return self.cleaned_data['situacao'].upper()

    def clean_observacao(self):
        return self.cleaned_data['observacao'].upper()
