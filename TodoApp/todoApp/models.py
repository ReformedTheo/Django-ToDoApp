from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS_CHOICES = [
    ('To do', 'TO DO'),
    ('in progress', 'IN PROGRESS'),
    ('Done', 'DONE'),
]

class Evento(models.Model):
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário", blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    date = models.DateField()
