from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class TipoSangue(models.Model):
    tipo = models.CharField(max_length=45,null=False,blank=False)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.tipo

class Hospital(models.Model):
    cnpj = models.CharField(max_length=45,null=False,blank=False)
    nome = models.CharField(max_length=200,null=False,blank=False)
    endereco = models.CharField(max_length=200,null=False,blank=False)
    telefone = models.CharField(max_length=15,null=False,blank= False)
    email = models.EmailField(max_length=45,null=False,blank=False)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=45,null=False,blank= False)
    cpf = models.BigIntegerField(null=False,blank=False)
    endereco = models.CharField(max_length=210,null=False,blank=False)
    telefone = models.CharField(max_length=15,null=False,blank=False)
    usuario = models.ForeignKey(User, null=False, on_delete=models.CASCADE,blank=False,default=1)

    PRIORIDADE_CHOICES = [
        ('S','Sim'),
        ('N','Não')
    ]

        
    prioridade = models.CharField(max_length=1,choices= PRIORIDADE_CHOICES, null=False,blank=False,default='N')

    def __str__(self):
        return str(self.nome)

class Dispersao(models.Model):
    cod_func= models.ForeignKey(Funcionario, on_delete=models.CASCADE,null=False,blank=False)
    cod_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,null=False,blank=False)
    cod_tiposang = models.ForeignKey(TipoSangue, on_delete=models.CASCADE,null=False,blank=False)
    qtd_bolsa = models.IntegerField(null=False,blank=False)
    data = models.DateField(null=False,blank=False)

class Doador(models.Model):
    cod_tiposang = models.ForeignKey(TipoSangue, on_delete=models.CASCADE,null=False,blank=False)
    nome = models.CharField(max_length=100,null=False,blank=False)
    endereco = models.CharField(max_length=200,null=False,blank=False)
    cpf = models.BigIntegerField(null=False,blank=False)
    telefone = models.CharField(max_length=15,null=False,blank=False)
    data_nascimento = models.DateField(null=False,blank=False)
    peso = models.CharField(max_length=20,null=False,blank=False)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    cod_doador = models.ForeignKey(Doador, on_delete=models.CASCADE, null=False,blank=False,default=1)
    data_hora = models.DateTimeField(null=False,blank=False)

    def __str__(self):
        return self.data_hora.strftime("%Y-%m-%d %H:%M:%S")

class Doacao(models.Model):
    cod_agen = models.ForeignKey(Agendamento, on_delete=models.CASCADE,null=False,blank=False)
    cod_func = models.ForeignKey(Funcionario, on_delete=models.CASCADE,null=False,blank=False)
    data_hora = models.DateTimeField(null=False,blank=False)

