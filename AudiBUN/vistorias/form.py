from django import forms
from django.forms import ModelForm, modelformset_factory

from AudiBUN.empresas.models import EmpresaModel
from AudiBUN.vistorias.models import VistoriaModel
'''
VistoriaForm = modelformset_factory(VistoriaModel, exclude=['created_at'])
VistoriaForm.queryset=EmpresaModel.objects.all()
vistoria_form = VistoriaForm(queryset=EmpresaModel.objects.all())

'''
class VistoriaForm(ModelForm):
    class Meta:
        model = VistoriaModel
        exclude = ['created_at']
        widgets = {
             'empresa': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }