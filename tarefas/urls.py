from django.urls import path
from . import views


urlpatterns = [
    path('', views.tarefas_pendentes_list.as_view(), name='tarefas_pendentes_list')
]