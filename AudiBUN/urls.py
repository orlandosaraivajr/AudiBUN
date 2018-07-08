from django.contrib import admin
from django.urls import path

import AudiBUN.core.views
import AudiBUN.empresas.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', AudiBUN.core.views.home),
    path('', AudiBUN.core.views.home),
    path('cadastroEmpresa/', AudiBUN.empresas.views.cadastro),
    path('login/', AudiBUN.core.views.login),
]
