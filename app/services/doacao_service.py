from ..models import Doacao

def inserir_doacao(doacao):
    doacao.objects.create(cod_agen=doacao.cod_agen, cod_func=doacao.cod_func,data_hora=doacao.data_hora)