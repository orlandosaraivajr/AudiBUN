from django.urls import path, include

urlpatterns = [
    path('', include('AudiBUN.core.urls')),
    path('empresa/', include('AudiBUN.empresas.urls')),
]

