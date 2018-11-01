from django.urls import path
from . import views

app_name = 'vistorias'

urlpatterns = [
    path('', views.listar, name='vistorias_listar_todas'),
    path('cadastro', views.cadastro, name='vistorias_cadastrar'),
    path('cadastro/<int:id_vistoria>/', views.visualizar, name='vistorias_listar'),
]
