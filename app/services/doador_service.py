from ..models import Doador

def cadastrar_doador(doador):
    Doador.objects.create(nome=doador.nome, endereco=doador.endereco, cpf=doador.cpf,
                            telefone=doador.telefone, data_nascimento=doador.data_nascimento,peso=doador.peso,
                            cod_tiposang=doador.cod_tiposang)
    

def listar_doador(usuario):
    # igual a select * from app_doador order by nome
    return Doador.objects.all().order_by('nome')

def listar_doador_id(id):
    return Doador.objects.get(id=id)


# recebe o lembrete já inserido no bd e o novo
def editar_doador(doador_bd, novo_doador):
    doador_bd.nome = novo_doador.nome
    doador_bd.endereco = novo_doador.endereco
    doador_bd.cpf = novo_doador.cpf
    doador_bd.telefone=novo_doador.telefone
    doador_bd.data_nascimento= novo_doador.data_nascimento
    novo_doador.peso = doador_bd.peso
    doador_bd.cod_tiposang = novo_doador.cod_tiposang
    doador_bd.save(force_update=True)


def excluir_doador(doador_bd):
    doador_bd.delete()