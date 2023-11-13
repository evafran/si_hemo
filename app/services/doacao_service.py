from ..models import Doacao

def inserir_doacao(doacao):
    Doacao.objects.create(cod_agen=doacao.cod_agen, cod_func=doacao.cod_func,data_hora=doacao.data_hora)


def listar_doacao(id):
    # igual a select * from app_doador order by nome
    return Doacao.objects.all().order_by('data_hora')

def listar_doacao_id(id):
    return Doacao.objects.get(id=id)


# recebe o doaçao já inserido no bd e o novo
def editar_doacao(doacao_bd, novo_doacao):
    doacao_bd.cod_agen = novo_doacao.cod_agen
    doacao_bd.cod_func = novo_doacao.cod_func
    doacao_bd.data_hora = novo_doacao.data_hora
    doacao_bd.save(force_update=True)


def excluir_doacao(doacao_bd):
    doacao_bd.delete()

