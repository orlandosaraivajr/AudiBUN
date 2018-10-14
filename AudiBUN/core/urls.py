from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.home, name='index'),
    path('', views.home,name='home'),
    path('empresas/', include('AudiBUN.empresas.urls')),
    path('vistorias/', include('AudiBUN.vistorias.urls')),
    path('login/', views.login, name='login'),
]