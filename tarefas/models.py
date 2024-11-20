from django.db import models

# modelos aqui
# class Usuario(models.Model):
#     nome = models.CharField(max_length=255, default='nome')
#     email = models.EmailField(max_length=255)


class Tarefa(models.Model):
    OPCOES_STATUS = (

        ('concluido', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
    )

    OPCOES_CATEGORIA = (

        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser Feito'),
    )

    descricao = models.CharField(max_length=255)
    criacao = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=25, choices=OPCOES_CATEGORIA, default='importante')
    status = models.CharField(max_length=25, choices=OPCOES_STATUS, default='pendente')