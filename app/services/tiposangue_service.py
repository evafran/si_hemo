from ..models import TipoSangue

def cadastrar_tiposangue(tiposangue):
    TipoSangue.objects.create(tipo=tiposangue.tipo, quantidade=tiposangue.quantidade)



def listar_tiposangue(id):
    # igual a select * from app_doador order by nome
    return TipoSangue.objects.all().order_by('tipo')

def listar_tiposangue_id(id):
    return TipoSangue.objects.get(id=id)


# recebe o tiposangue já inserido no bd e o novo
def editar_tiposangue(tiposangue_bd, novo_tiposangue):
    tiposangue_bd.tipo = novo_tiposangue.tipo
    tiposangue_bd.quantidade = novo_tiposangue.quantidade
    tiposangue_bd.save(force_update=True)


def excluir_tiposangue(tiposangue_bd):
    tiposangue_bd.delete()

