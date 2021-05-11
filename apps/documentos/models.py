from apps.funcionarios.models import Funcionario
from django.db import models

class Documentos(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao