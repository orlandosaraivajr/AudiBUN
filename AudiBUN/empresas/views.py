from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from AudiBUN.empresas.form import EmpresaForm
from AudiBUN.empresas.models import EmpresaModel
from AudiBUN.empresas.models import DISTRITO_CHOICES

@login_required
def cadastro(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

@login_required
def new(request):
    context = {'form': EmpresaForm()}
    return render(request, 'empresas_cadastro.html', context)

@login_required
def create(request):
    form = EmpresaForm(request.POST)
    if not form.is_valid():
        return render(request, 'empresas_cadastro.html',
                      {'form': form})
    else:
        EmpresaModel.objects.create(**form.cleaned_data)
        # Sucess feedback
#        messages.success(request, 'Inscrição Realizada com Sucesso !')
        return HttpResponseRedirect(reverse('home'))


@login_required
def editar(request):
    context = {'form': EmpresaForm(),
               'empresas': EmpresaModel.objects.all()}
    return render(request, 'empresas_listar_editar.html', context)


@login_required
def editar_empresa(request, id_empresa):
    id = id_empresa
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if not form.is_valid():
            erros = ''
            for e in form.errors:
                erros += form.errors[e]
            # Fail feedback
            messages.error(request, erros)
            context = {'form': form}
        else:
            EmpresaModel.objects.filter(pk=id).update(**form.cleaned_data)
            # Sucess feedback
            messages.success(request, 'Atualização Realizada com Sucesso !')
            obj = get_object_or_404(EmpresaModel, pk=id)
            form = EmpresaForm(instance=obj)
            context = {'form': form}
        return render(request, "empresas_editar.html", context)
    else:
        obj = get_object_or_404(EmpresaModel, pk=id)
        form = EmpresaForm(instance=obj)
        context = {'form': form}
        return render(request, "empresas_editar.html", context)

@login_required
def visualizar_empresa(request, id_empresa):
    id = id_empresa
    obj = get_object_or_404(EmpresaModel, pk=id)
    form = EmpresaForm(instance=obj)
    form.read_only()
    context = {'form': form}
    return render(request, "empresas_visualizar.html", context)
