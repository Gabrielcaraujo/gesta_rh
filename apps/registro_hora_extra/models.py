from apps.funcionarios.models import Funcionario
from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo