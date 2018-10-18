from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from AudiBUN.vistorias.form import VistoriaForm
from AudiBUN.vistorias.models import VistoriaModel


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
        return HttpResponseRedirect(reverse('home'))

def visualizar(request):
    return HttpResponse('em desenvolvimento')

def editar(request):
    return HttpResponse('em desenvolvimento')

def editar_vistoria(request):
    return HttpResponse('em desenvolvimento')