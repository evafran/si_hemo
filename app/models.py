from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class TipoSangue(models.Model):
    TIPO = models.CharField(max_length=45)
    QUANTIDADE = models.IntegerField()

class Hospital(models.Model):
    CNPJ = models.CharField(max_length=45)
    NOME = models.CharField(max_length=200)
    ENDERECO = models.CharField(max_length=200)
    TELEFONE = models.CharField(max_length=15)
    EMAIL = models.CharField(max_length=45)

class Funcionario(models.Model):
    NOME = models.CharField(max_length=45)
    CPF = models.BigIntegerField()
    ENDERECO = models.CharField(max_length=210)
    TELEFONE = models.CharField(max_length=15)
    USUARIO = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class Dispersao(models.Model):
    COD_FUNC = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    COD_HOSPITAL = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    COD_TIPOSANG = models.ForeignKey(TipoSangue, on_delete=models.CASCADE)
    QTD_BOLSA = models.CharField(max_length=45)
    DATA = models.DateField()

class Doador(models.Model):
    COD_TIPOSANG = models.ForeignKey(TipoSangue, on_delete=models.CASCADE)
    NOME = models.CharField(max_length=100)
    ENDERECO = models.CharField(max_length=200)
    CPF = models.BigIntegerField()
    TELEFONE = models.CharField(max_length=15)
    DATA_NASCIMENTO = models.DateField()
    PESO = models.CharField(max_length=20)

class Agendamento(models.Model):
    COD_DOADOR = models.ForeignKey(Doador, on_delete=models.CASCADE, null=True)
    DIA_DISPONIVEL = models.CharField(max_length=45)
    DATA_HORA = models.DateTimeField()

class Doacao(models.Model):
    COD_AGEN = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    COD_FUNC = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    DATA_HORA = models.DateTimeField()

