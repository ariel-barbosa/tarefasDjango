from django.shortcuts import render
from .models import Tarefa, Usuario
from django.views.generic.edit import *
from django.views.generic.list import *


class tarefas_list(ListView):
    template_name = 'tarefas/index.html'
    model = Tarefa
    context_object_name = 'tarefas'


class usuario_list(ListView):
    template_name = 'usuarios.html'
    model = Usuario
    context_object_name = 'usuarios'

# def tarefas_pendentes_list(request):
#     tarefas_pendentes = Tarefa.objects.all
#     return render(request, 'tarefas/index.html',
#                   {'tarefas_pendentes':tarefas_pendentes})

# def usuario_list(request):
#     usuario_list = Usuario.object.all
#     return render(request, 'tarefas/usuario_list.html',
#                 {'usuario_list':usuario_list})