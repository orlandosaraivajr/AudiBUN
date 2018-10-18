from django.urls import path
from . import views

app_name = 'vistorias'

urlpatterns = [
    path('', views.listar, name='vistorias_listar_todas'),
    path('cadastro', views.cadastro, name='vistorias_cadastrar'),
    path('cadastro/<int:id_vistoria>/', views.visualizar, name='vistorias_listar'),
    path('editar/', views.editar, name='vistorias_listar_editar'),
    path('editar/<int:id_vistoria>/', views.editar_vistoria, name='vistorias_editar'),
]
