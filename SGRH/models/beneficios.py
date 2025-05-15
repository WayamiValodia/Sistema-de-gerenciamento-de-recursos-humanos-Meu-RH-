from django.db import models
from .funcionario import Funcionario
from .geral import Geral

class Beneficio(Geral):
  Tipo=[
    ('T', 'Transporte'),
    ('R', 'Refeição')
    ]
  Status =[
    ('B', 'Beneficiado'),
    ('N', 'Não beneficiado')
    ]
    
  funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
  valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  tipo = models.CharField(choices=Tipo, max_length=1)
  descricacao = models.CharField(max_length=225)
  status = models.CharField(choices=Status, max_length=1)
    
  def __str__(self):
    return self.funcionario.nome