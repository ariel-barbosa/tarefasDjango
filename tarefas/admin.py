from django.contrib import admin
from .models import Tarefa, Usuario

# user: ariel
# emial: admin@email.com
# senha: ariel123

# Registrar modelo
admin.site.register(Tarefa)
admin.site.register(Usuario)
