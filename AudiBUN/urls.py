from django.contrib import admin
from django.urls import path

import AudiBUN.core.views
import AudiBUN.empresas.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', AudiBUN.core.views.home),
    path('', AudiBUN.core.views.home),
    path('cadastroEmpresa/', AudiBUN.empresas.views.cadastro),
    path('cadastroEmpresa/<int:id_empresa>/', AudiBUN.empresas.views.visualizar_empresa),
    path('editarEmpresa/', AudiBUN.empresas.views.editar),
    path('editarEmpresa/<int:id_empresa>/', AudiBUN.empresas.views.editar_empresa),
    path('login/', AudiBUN.core.views.login),
]
