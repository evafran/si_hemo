from django.shortcuts import render,redirect
from ...forms import HospitalForm
from ...entidades.hospital import Hospital
from ...services import hospital_service
from django.contrib.auth.decorators import login_required
  

@login_required()

def cadastrar_hospital(request):
    if request.method == 'POST':
        # se o método for == POST, vai passar os dados da requisição para o formulário
        form_hospital= HospitalForm(request.POST)
        if form_hospital.is_valid():
            # captura as infos que vieram do formulário
            cnpj = form_hospital.cleaned_data['cnpj']
            nome = form_hospital.cleaned_data['nome']
            endereco = form_hospital.cleaned_data['endereco']
            telefone = form_hospital.cleaned_data['telefone']
            email = form_hospital.cleaned_data['email']
            novo_hospital = Hospital(cnpj=cnpj, nome=nome, endereco=endereco,telefone=telefone,email=email)
            # envia o objeto com os dados para o hospital_service, que insere no BD
            hospital_service.cadastrar_hospital(novo_hospital)
            return redirect('listar_agendamentos')
    else:
        # cria uma instância vazia do formulário caso o método não seja POST
        form_hospital = HospitalForm()
    return render(request, 'hospital/form_hospital.html', {'form_hospital': form_hospital})




# com login_required exibe o método apenas se o usuário estiver logado, se não, redireciona para página de login
@login_required()
def listar_hospital(request):
    hospital = hospital_service.listar_hospital(request.user)
    return render(request, 'hospital/listar_hospital.html', {'hospital': hospital})

@login_required()
def editar_hospital(request,id):
    # armazena o hospital que o usuário está buscando através do cnpj
    hospital_bd = hospital_service.listar_hospital_id(id)
    # aviso caso o usuário tente editar um hospital que ele nao tem acesso, através da url
    form_hospital = HospitalForm(request.POST or None, instance=hospital_bd)
    if form_hospital.is_valid():
        cnpj = form_hospital.cleaned_data['cnpj']
        nome = form_hospital.cleaned_data['nome']
        endereco = form_hospital.cleaned_data['endereco']
        telefone =form_hospital.cleaned_data['telefone']
        email= form_hospital.cleaned_data['email']
        
        novo_hospital = Hospital( cnpj= cnpj, nome=nome, endereco=endereco,telefone=telefone, email= email)
        hospital_service.editar_hospital(hospital_bd, novo_hospital)
        return redirect('listar_hospital')

    return render(request, 'hospital/form_hospital.html', {'form_hospital': form_hospital})


@login_required()
def excluir_hospital(request, id):
    hospital_bd = hospital_service.listar_hospital_id(id)
    if request.method == 'POST':
        hospital_service.excluir_hospital(hospital_bd)
        return redirect('listar_hospital')
    return render(request, 'hospital/confirmar_exclusao_hospital.html', {'hospital': hospital_bd})


