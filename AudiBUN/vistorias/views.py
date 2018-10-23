from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from AudiBUN.vistorias.form import VistoriaForm
from AudiBUN.vistorias.models import VistoriaModel


def listar(request):
    context = {'form': VistoriaForm(),
               'vistorias': VistoriaModel.objects.all()}
    return render(request, 'vistorias_listar_todas.html', context)


def cadastro(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    context = {'form': VistoriaForm()}
    return render(request, 'vistorias_cadastro.html', context)


def create(request):
    form = VistoriaForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'vistorias_cadastro.html',
                      {'form': form})
    else:
        VistoriaModel.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(reverse('vistorias:vistorias_listar_todas'))

def visualizar(request, id_vistoria):
    id = id_vistoria
    obj = get_object_or_404(VistoriaModel, pk=id)
    form = VistoriaForm(instance=obj)
    form.read_only()
    context = {
        'form': form,
        'vistoria': obj
    }
    return render(request, "vistorias_visualizar.html", context)


def editar(request):
    return HttpResponse('em desenvolvimento: editar todas as vistorias')

def editar_vistoria(request, id_vistoria):
    return HttpResponse('em desenvolvimento: editar apenas uma vistoria')