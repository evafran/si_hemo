from ..models import Dispersao

def solicitar_dispersao(dispersao):
    Dispersao.objects.create(cod_func=dispersao.cod_func, cod_hospital=dispersao.cod_hospital, cod_tiposang=dispersao.cod_tiposang,
                            qtd_bolsa=dispersao.qtd_bolsa, data=dispersao.data)