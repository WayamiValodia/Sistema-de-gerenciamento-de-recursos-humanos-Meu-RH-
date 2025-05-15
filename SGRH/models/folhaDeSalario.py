from django.db import models
from .geral import Geral
from .funcionario import Funcionario

class Folha(Geral):
  funcionario = models.ForeignKey(Funcionario, on_delete = models.CASCADE)
  mes_ano = models.DateField()
  salario_bruto=models.DecimalField(max_digits=10, decimal_places=2)
  descontos = models.DecimalField(max_digits=10, decimal_places=2)
  salario_liquido = models.DecimalField(max_digits=10, decimal_places=2)
  
  def __str__(self):
    return (f"Funcionário:{self.funcionario.nome}," f"Mês/Ano:{self.mes_ano.strftime('%Y-%M')},"f"Descontos:{self.descontos}")