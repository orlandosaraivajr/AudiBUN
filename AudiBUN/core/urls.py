from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('index', views.home, name='index'),
    path('', views.home,name='root'),
    path('login/', views.login, name='login'),
]