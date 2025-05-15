from django.db import models
from .funcionario import Funcionario
from .geral import Geral

class Feria(Geral):
  Status=[
    ('A','Aprovada'),
    ('R', 'Rejeitada')
    ]
    
  funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
  status = models.CharField(choices=Status, max_length=1)
  data_inicio = models.DateField()
  data_fim = models.DateField()
  
  def __str__(self):
    return self.funcionario.nome