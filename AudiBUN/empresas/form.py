from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from AudiBUN.empresas.models import EmpresaModel, ATIVIDADE_CHOICES, DISTRITO_CHOICES


class EmpresaForm(ModelForm):
    class Meta:
        model = EmpresaModel
        exclude = ['created_at']

        labels = {
            'ref_cad': 'RC',
            'area_lote': 'Área do Lote',
            'area_construida': 'Área Construída',
            'name': 'Empresa',
            'cnpj': 'CNPJ',
            'categoria_atividade': 'Atividade',
            'atividade': 'Descrição da atividade',
            'endereco': 'Endereço',
            'quadra': 'Quadra',
            'lote': 'Lt',
            'categoria_distrito': 'Distrito',
            'email': 'E-mail',
            'phone': 'Fone',
            'responsavel': 'Responsável',
            'situacao': 'Situação',
            'observacao' : 'Observação',
        }
        widgets = {
            'ref_cad': forms.TextInput(attrs={'class': 'form-control'}),
            'area_lote': forms.TextInput(attrs={'class': 'form-control'}),
            'area_construida': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_atividade': forms.Select(choices=ATIVIDADE_CHOICES,attrs={'class': 'form-control'}),
            'atividade': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'quadra': forms.TextInput(attrs={'class': 'form-control'}),
            'lote': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_distrito': forms.Select(choices=DISTRITO_CHOICES, \
                                               attrs={'class': 'form-control',
                                                      'onChange': 'change_click_categoria_distrito()',
                                                      }),

            'bairro': forms.TextInput(attrs={'class': 'form-control',\
                                            'onClick': 'change_distrito_click_bairro()',
                                                      }),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'situacao': forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control',
                                                'rows' : '7', 'cols' : '50'
        }),
        }
        help_texts = {
            'ref_cad': ('Referência Cadastral.'),
            'name': ('Nome da Empresa.'),
        }
        error_messages = {
            'ref_cad': {
                'required': ("Referência cadastral não pode ser em branco."),
            },
            'quadra': {
                'required': ("Quadra não pode ser em branco."),
            },
            'lote': {
                'required': ("Lote não pode ser em branco."),
            },
            'name': {
                'max_length': ("Nome da empresa ultrapassa limite máximo de caracteres."),
                'required': ("Nome da empresa não pode ser em branco."),
            },
            'situacao': {
                'required': ("Situação da empresa não pode ser em branco."),
            },
        }

    def clean_cnpj(self):
        '''Validate CNPJ field in the format: 00.000.000/0000-00 '''
        cnpj = self.cleaned_data['cnpj']
        try:
            sub1, sub2 = cnpj.split('/')
            valores = sub1.split('.')
        except:
            self.cleaned_data['cnpj'] = '00.000.000/0000-00'
            cnpj = self.cleaned_data['cnpj']
        sub1, sub2 = cnpj.split('/')
        valores = sub1.split('.')
        for v in valores:
            try:
                int(v)
            except:
                raise ValidationError('CNPJ pode conter apenas números no formato: 00.000.000/0000-00')
        valores = sub2.split('-')
        for v in valores:
            try:
                int(v)
            except:
                raise ValidationError('CNPJ pode conter apenas números no formato: 00.000.000/0000-00')
        return self.cleaned_data['cnpj']

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

    def clean_area_lote(self):
        return  self.cleaned_data['area_lote'].upper()

    def clean_area_construida(self):
        return  self.cleaned_data['area_construida'].upper()

    def clean_quadra(self):
        return self.cleaned_data['quadra'].upper()

    def clean_atividade(self):
        return self.cleaned_data['atividade'].upper()

    def clean_endereco(self):
        return self.cleaned_data['endereco'].upper()

    def clean_bairro(self):
        return  self.cleaned_data['bairro'].upper()

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