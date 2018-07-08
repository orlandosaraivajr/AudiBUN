from django.shortcuts import render

from AudiBUN.empresas.form import EmpresaForm
from AudiBUN.empresas.models import EmpresaModel


def home(request):
    context = {'form': EmpresaForm(),
               'empresas': EmpresaModel.objects.all()}
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')
