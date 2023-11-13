from ..models import Hospital

def cadastrar_hospital(hospital):
    Hospital.objects.create(cnpj=hospital.cnpj, nome=hospital.nome, endereco=hospital.endereco,
                            telefone=hospital.telefone, email=hospital.email)
    

def listar_hospital(id):
    # igual a select * from app_doador order by nome
    return Hospital.objects.all().order_by('nome')

def listar_hospital_id(id):
    return Hospital.objects.get(id=id)


# recebe o hospital já inserido no bd e o novo
def editar_hospital(hospital_bd, novo_hospital):
    hospital_bd.cnpj = novo_hospital.cnpj
    hospital_bd.nome = novo_hospital.nome
    hospital_bd.endereco = novo_hospital.endereco
    hospital_bd.telefone=novo_hospital.telefone
    hospital_bd.email= novo_hospital.email
    hospital_bd.save(force_update=True)


def excluir_hospital(hospital_bd):
    hospital_bd.delete()

