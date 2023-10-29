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
