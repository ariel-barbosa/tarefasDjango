from django.urls import path
from . import views


urlpatterns = [
    path('', views.tarefas_list.as_view(), name='tarefas_list'),
    path('usuario/', views.usuario_list.as_view(), name='usuario_list')
]