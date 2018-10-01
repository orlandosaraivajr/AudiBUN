from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from AudiBUN.empresas.form import EmpresaForm
from AudiBUN.empresas.models import EmpresaModel


def cadastro(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    context = {'form': EmpresaForm()}
    return render(request, 'cadastro.html', context)


def create(request):
    form = EmpresaForm(request.POST)
    if not form.is_valid():
        return render(request, 'cadastro.html',
                      {'form': form})
    else:
        EmpresaModel.objects.create(**form.cleaned_data)
        # Sucess feedback
        messages.success(request, 'Inscrição Realizada com Sucesso !')
        return HttpResponseRedirect('/')


def editar(request):
    context = {'form': EmpresaForm(),
               'empresas': EmpresaModel.objects.all()}
    return render(request, 'empresas.html', context)


def editar_empresa(request, id_empresa):
    id = id_empresa
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if not form.is_valid():
            context = {'form': EmpresaForm(),
                       'empresas': EmpresaModel.objects.all()}
            return render(request, 'empresas.html', context)
        else:
            EmpresaModel.objects.filter(pk=id).update(**form.cleaned_data)
            # Sucess feedback
            messages.success(request, 'Atualização Realizada com Sucesso !')
            context = {'form': form}
            return render(request, "editar.html", context)
    else:
        obj = get_object_or_404(EmpresaModel, pk=id)
        form = EmpresaForm(instance=obj)
        context = {'form': form}
        return render(request, "editar.html", context)
