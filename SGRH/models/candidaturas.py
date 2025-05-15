from django.db import models
from .areas import Areas

class Candidatura(models.Model):
  Status = [
    ('EA', 'Em análise'),
    ('C', 'Contratado'),
    ('R', 'Rejeito')
  ]
  
  nome_candidato = models.CharField(max_length = 100)
  data = models.DateField()
  area = models.ForeignKey(Areas, on_delete = models.CASCADE)
  status = models.CharField(choices = Status, max_length = 2)

  def __str__(self):
    return self.nome_candidato