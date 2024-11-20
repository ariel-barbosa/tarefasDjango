from django.shortcuts import render

from tarefas.models import Tarefa

# Crie views aqui.
def tarefas_pendentes_list(request):
    tarefas_pendentes = Tarefa.objects.filter(status='pendente')
    return render(request, 'tarefas/tarefas_pendentes.html',
                  {'tarefas_pendentes':tarefas_pendentes})

from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")  # Render a template

