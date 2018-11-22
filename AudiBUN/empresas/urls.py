from django.urls import path
from . import views

app_name = 'empresas'

urlpatterns = [
    path('', views.cadastro, name='empresas_cadastrar'),
    path('cadastro/<int:id_empresa>/', views.visualizar_empresa, name='empresas_listar'),
    path('editar/', views.editar, name='empresas_listar_editar'),
    path('editar/<int:id_empresa>/', views.editar_empresa, name='editar'),
    path('vistorias/<int:id_empresa>/', views.vistorias_empresa, name='empresas_vistorias'),
]
