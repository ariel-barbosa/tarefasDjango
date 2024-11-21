CREATE DATABASE db_tarefas;
USE db_tarefas;

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
    
CREATE TABLE tarefas (
    id SERIAL PRIMARY KEY AUTO_INCREMENT NOT NULL, -- Identificador único (opcional, mas geralmente útil)
    descricao TEXT NOT NULL, -- Descrição da tarefa
    criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, -- Data e hora de criação da tarefa
    categoria VARCHAR(50) NOT NULL, -- Categoria da tarefa (ajuste o tamanho conforme necessário)
    tar_status VARCHAR(20) NOT NULL -- Status da tarefa com valor padrão 'pendente'
);
