# Create your models here.
from django.db import models


class Voluntario(models.Model):
    """voluntario model"""
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)

    def __str__(self):
        """Return the model as String"""
        return f'{self.nome} {self.sobrenome}'


class Acao(models.Model):
    """Ação model"""
    nome_acao = models.CharField(max_length=30)
    instituicao_organizadora = models.CharField(max_length=30)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        """Return the model as String"""
        return f'{self.nome_acao} - {self.instituicao_organizadora}'
