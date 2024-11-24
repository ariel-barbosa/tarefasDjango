from django.shortcuts import render
from .models import Tarefa
from django.views.generic.edit import *
from django.views.generic.list import *


def tarefas_pendentes_list(request):
    tarefas_pendentes =  Tarefa.objects.filter(status='pendente')
    return render(request, 'tarefas/tarefas_pendentes.html',
                {'tarefas':tarefas_pendentes})





