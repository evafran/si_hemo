from ..models import Dispersao

def solicitar_dispersao(dispersao):
    Dispersao.objects.create(cod_func=dispersao.cod_func, cod_hospital=dispersao.cod_hospital, cod_tiposang=dispersao.cod_tiposang,
                            qtd_bolsa=dispersao.qtd_bolsa, data=dispersao.data)


def listar_dispersao(id):
    # igual a select * from app_dispersao order by data
    return Dispersao.objects.all().order_by('-data')

def listar_dispersao_id(id):
    return Dispersao.objects.get(id=id)


# recebe o dispersao já inserido no bd e o novo
def editar_dispersao(dispersao_bd, novo_dispersao):
    dispersao_bd.cod_func = novo_dispersao.cod_func
    dispersao_bd.cod_hospital = novo_dispersao.cod_hospital
    dispersao_bd.cod_tiposang = novo_dispersao.cod_tiposang
    dispersao_bd.qtd_bolsa = novo_dispersao.qtd_bolsa
    dispersao_bd.data = novo_dispersao.data
    dispersao_bd.save(force_update=True)


def excluir_dispersao(dispersao_bd):
    dispersao_bd.delete()

