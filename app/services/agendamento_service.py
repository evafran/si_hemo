from ..models import Agendamento

def listar_agendamentos(usuario):
    #igual o select * from app_agendamento  order by data_hora 
    return Agendamento.objects.all().order_by('data_hora')

def cadastrar_agendamento(agendamento):
    Agendamento.objects.create(cod_doador=agendamento.cod_doador,data_hora=agendamento.data_hora)