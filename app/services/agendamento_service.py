from ..models import Agendamento

def listar_agendamentos(usuario):
    #igual o select * from app_agendamento  order by data_hora 
    return Agendamento.objects.all().order_by('data_hora')

def cadastrar_agendamento(agendamento):
    Agendamento.objects.create(cod_doador=agendamento.cod_doador,data_hora=agendamento.data_hora)


def listar_agendamento_id(id):
    return Agendamento.objects.get(id=id)


# recebe o agendamento  já inserido no bd e o novo

def editar_agendamento(agendamento_bd, novo_agendamento):
    agendamento_bd.cod_doador= novo_agendamento.cod_doador
    agendamento_bd.data_hora= novo_agendamento.data_hora
    agendamento_bd.save(force_update=True)


def excluir_agendamento(agendamento_bd):
    agendamento_bd.delete()