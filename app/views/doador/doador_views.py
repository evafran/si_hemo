from django.shortcuts import render,redirect
from ...forms import DoadorForm
from ...entidades.doador import Doador
from ...services import doador_service
from django.contrib.auth.decorators import login_required

@login_required()

def cadastrar_doador(request):
    if request.method == 'POST':
        # se o método for == POST, vai passar os dados da requisição para o formulário
        form_doador= DoadorForm(request.POST)
        if form_doador.is_valid():
            # captura as infos que vieram do formulário
            nome = form_doador.cleaned_data['nome']
            endereco = form_doador.cleaned_data['endereco']
            cpf = form_doador.cleaned_data['cpf']
            telefone = form_doador.cleaned_data['telefone']
            data_nascimento = form_doador.cleaned_data['data_nascimento']
            peso = form_doador.cleaned_data['peso']
            cod_tiposang = form_doador.cleaned_data['cod_tiposang']
            novo_doador = Doador(nome=nome, endereco=endereco, cpf=cpf,telefone=telefone,
                                    data_nascimento=data_nascimento, peso= peso,cod_tiposang=cod_tiposang)
            # envia o objeto com os dados para o doador_service, que insere no BD
            doador_service.cadastrar_doador(novo_doador)
            return redirect('listar_agendamentos')
    else:
        # cria uma instância vazia do formulário caso o método não seja POST
        form_doador = DoadorForm()
    return render(request, 'doador/form_doador.html', {'form_doador': form_doador})


