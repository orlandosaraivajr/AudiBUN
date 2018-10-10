from django.urls import path
from . import views

app_name = 'vistorias'
urlpatterns = [
    path('', views.cadastro, name='cadastrar'),
    path('cadastro/<int:id_empresa>/', views.visualizar, name='listar'),
    path('editar/', views.editar, name='listar_editar'),
    path('editar/<int:id_vistoria>/', views.editar_vistoria, name='editar'),
]
