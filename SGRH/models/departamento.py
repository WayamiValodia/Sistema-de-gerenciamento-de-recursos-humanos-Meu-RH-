from django.db import models
from .geral import Geral

class Departamento(Geral):
  nome = models.CharField(max_length=125)
  
  def __str__(self):
    return self.nome