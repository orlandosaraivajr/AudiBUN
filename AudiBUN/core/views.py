from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from AudiBUN.empresas.form import EmpresaForm
from AudiBUN.empresas.models import EmpresaModel

@login_required
def home(request):
    context = {'form': EmpresaForm(),
               'empresas': EmpresaModel.objects.all()}
    return render(request, 'index.html', context)


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            context = {'form': EmpresaForm(),
                       'empresas': EmpresaModel.objects.all()}
            return render(request, 'index.html', context)
        else:
            context = {'acesso_negado': True}
            return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')