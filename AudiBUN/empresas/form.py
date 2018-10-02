from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.utils import ErrorList

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
        error = {
            'quadra': 'Campo Quadra obrigatório'
        }

    def clean_ref_cad(self):
        referencia_cadastral = self.cleaned_data['ref_cad']
        lista_ref_cad = referencia_cadastral.split('.')
        if len(lista_ref_cad) < 5 or len(lista_ref_cad) > 6:
            raise ValidationError('Formato incorreto do campo Referência Cadastral')
        try:
            int(lista_ref_cad[0])
        except:
            raise ValidationError('Quadricula precisa ser um número. Erro em Referência Cadastral')
        try:
            int(lista_ref_cad[1])
        except:
            raise ValidationError('Zona precisa ser um número. Erro em Referência Cadastral')
        try:
            int(lista_ref_cad[2])
        except:
            raise ValidationError('Setor precisa ser um número. Erro em Referência Cadastral')
        try:
            int(lista_ref_cad[4])
        except:
            raise ValidationError('Lote precisa ser um número. Erro em Referência Cadastral')
        return self.cleaned_data['ref_cad'].upper()

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

    def read_only(self, read_only=True):
        ''' Set fields with attribute readonly'''
        fields = list(self.fields)
        if read_only:
            for field in fields:
                self.fields[field].widget.attrs['readonly'] = True
        else:
            for field in fields:
                self.fields[field].widget.attrs['readonly'] = False

    def clean(self):
        self.cleaned_data = super().clean()

        return self.cleaned_data