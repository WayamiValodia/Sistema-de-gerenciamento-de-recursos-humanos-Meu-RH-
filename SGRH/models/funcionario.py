from django.db import models
from .geral import Geral
from .departamento import Departamento

class Funcionario(Geral):
  Genero = [
    ('M', 'Masculino'),
    ('F', 'Feminino')
    ]
    
  Status =[
    ('A', 'Activo'),
    ('I', 'Inactivo')
    ]
    
  departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, related_name='id_departamento')
  nome = models.CharField(max_length=100)
  data_nascimento = models.DateField()
  bilhete = models.CharField(max_length=14, unique=True)
  cargo = models.CharField(max_length=100)
  data_contratacao = models.DateField()
  salario_base = models.DecimalField(max_digits=10, decimal_places=2)
  genero = models.CharField(choices=Genero, max_length=1)
  status = models.CharField(choices=Status, max_length=1)
  

  def __str__(self):
    return self.nome
    