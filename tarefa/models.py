from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('em_andamento', 'Em andamento'),
        ('finalizada', 'Finalizada'),
    ]
    
    id = models.AutoField(primary_key=True)
    nome_tarefa = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em_andamento')

    def __str__(self):
        return f"{self.nome_tarefa} - {self.descricao} - {self.date}"
