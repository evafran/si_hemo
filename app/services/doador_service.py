from ..models import Doador

def cadastrar_doador(doador):
    Doador.objects.create(nome=doador.nome, endereco=doador.endereco, cpf=doador.cpf,
                            telefone=doador.telefone, data_nascimento=doador.data_nascimento,peso=doador.peso,
                            cod_tiposang=doador.cod_tiposang)
