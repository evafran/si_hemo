from ..models import Hospital

def cadastrar_hospital(hospital):
    Hospital.objects.create(cnpj=hospital.cnpj, nome=hospital.nome, endereco=hospital.endereco,
                            telefone=hospital.telefone, email=hospital.email)