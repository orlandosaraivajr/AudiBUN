from django.urls import path
from . import views

app_name = 'empresas'
urlpatterns = [
    path('', views.cadastro, name='cadastrar'),
    path('cadastro/<int:id_empresa>/', views.visualizar_empresa, name='listar'),
    path('editar/', views.editar, name='listar_editar'),
    path('editar/<int:id_empresa>/', views.editar_empresa, name='editar'),
]
