from django.db import models
from .funcionario import Funcionario
from .geral import Geral

class Contacto(Geral):
  funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
  telefone = models.CharField(max_length=15, unique=True)
  email = models.EmailField(max_length=225, unique=True)
  
  def __str__(str):
    return f'Contacto de{self.Funcionario.nome}'