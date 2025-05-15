from django.db import models
from .funcionario import Funcionario
from .geral import Geral

class Ponto(Geral):
  funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
  data = models.DateField()
  hora_entrada = models.TimeField()
  hora_saida = models.TimeField()
  
  def __str__(self):
    return f'Registro de {self.funcionario.nome} em {self.data}'