from django.db import models

class Areas(models.Model):
  Status = [
    ('D', 'Disponível'),
    ('ND','Não disponível')
  ]

  area = models.CharField(max_length = 100)
  status = models.CharField(choices = Status, max_length = 2)

  def __str__(self):
    return f'Área: { self.area} Situação: { self.satus}'