from django.db import models
from django.contrib.auth.models import User

class Time(models.Model):
    STATUS_CHOICES = [
    ('acompanho', 'Acompanho'),
    ('nao_acompanho', 'Não acompanho'),
]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='acompanho')
    nota = models.IntegerField(null=True, blank=True)  # 1 a 5, opcional
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome