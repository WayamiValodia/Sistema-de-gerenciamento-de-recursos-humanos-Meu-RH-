from django.db import models
from .funcionario import Funcionario 
from .geral import Geral

class Treinamento(Geral):
  funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
  titulo = models.CharField(max_length=100)
  descricao = models.CharField(max_length=250)
  data = models.DateField()
  
  def __str__(self):
    return self.fumcionario.nome