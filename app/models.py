from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class TipoSangue(models.Model):
    tipo = models.CharField(max_length=45)
    quantidade = models.IntegerField()

class Hospital(models.Model):
    cnpj = models.CharField(max_length=45)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=45)

class Funcionario(models.Model):
    nome = models.CharField(max_length=45)
    cpf = models.BigIntegerField()
    endereco = models.CharField(max_length=210)
    telefone = models.CharField(max_length=15)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    PRIORIDADE_CHOICES = [
        ('S','Sim'),
        ('N','Não')
    ]

        
    prioridade = models.CharField(max_length=1,choices= PRIORIDADE_CHOICES, null=False,blank=False,default='N')

class Dispersao(models.Model):
    cod_func= models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cod_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    cod_tiposang = models.ForeignKey(TipoSangue, on_delete=models.CASCADE)
    qtd_bolsa = models.CharField(max_length=45)
    data = models.DateField()

class Doador(models.Model):
    cod_tiposang = models.ForeignKey(TipoSangue, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cpf = models.BigIntegerField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    peso = models.CharField(max_length=20)

class Agendamento(models.Model):
    cod_doador = models.ForeignKey(Doador, on_delete=models.CASCADE, null=True)
    dia_disponivel = models.CharField(max_length=45)
    data_hora = models.DateTimeField()

class Doacao(models.Model):
    cod_agen = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    cod_func = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()

