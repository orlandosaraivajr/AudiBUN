from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from AudiBUN.empresas.form import EmpresaForm
from AudiBUN.empresas.models import EmpresaModel


def cadastro(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    context = {'form':EmpresaForm()}
    return render(request, 'cadastro.html',context)

def create(request):

    form = EmpresaForm(request.POST)
    if not form.is_valid():
        return render(request, "cadastro.html",
                      {'form': form})
    else:
        EmpresaModel.objects.create(**form.cleaned_data)
        # Sucess feedback
        messages.success(request, 'Inscrição Realizada com Sucesso !')
        return HttpResponseRedirect('/cadastroEmpresa/')
