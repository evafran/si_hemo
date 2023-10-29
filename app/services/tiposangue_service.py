from ..models import TipoSangue

def cadastrar_tiposangue(tiposangue):
    TipoSangue.objects.create(tipo=tiposangue.tipo, quantidade=tiposangue.quantidade)