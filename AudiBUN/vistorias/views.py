from django.http import HttpResponse
from django.shortcuts import render

from AudiBUN.vistorias.form import VistoriaForm


def cadastro(request):
    form = VistoriaForm()
    context = {'form' : form}
    return render(request, 'vistorias_cadastro.html', context)

def visualizar(request):
    return HttpResponse('em desenvolvimento')

def editar(request):
    return HttpResponse('em desenvolvimento')

def editar_vistoria(request):
    return HttpResponse('em desenvolvimento')