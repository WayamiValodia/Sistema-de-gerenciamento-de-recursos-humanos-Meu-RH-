from django.db import models
from .departamento import Departamento
from .geral import Geral

class Cargo(Geral):
  nome = models.CharField(max_length=125)
  departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, related_name="id_cargos")
  
  def __str__(self): 
    return self.nome