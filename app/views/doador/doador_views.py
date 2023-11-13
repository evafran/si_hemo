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
            return redirect('listar_doador')
    else:
        # cria uma instância vazia do formulário caso o método não seja POST
        form_doador = DoadorForm()
    return render(request, 'doador/form_doador.html', {'form_doador': form_doador})


# com login_required exibe o método apenas se o usuário estiver logado, se não, redireciona para página de login
@login_required()
def listar_doador(request):
    doador = doador_service.listar_doador(request.user)
    return render(request, 'doador/listar_doador.html', {'doador': doador})



@login_required()
def editar_doador(request, id):
    # armazena o doador que o usuário está buscando através do id
    doador_bd = doador_service.listar_doador_id(id)
    # aviso caso o usuário tente editar um lembrete que ele nao tem acesso, através da url
    form_doador = DoadorForm(request.POST or None, instance=doador_bd)
    if form_doador.is_valid():
        nome = form_doador.cleaned_data['nome']
        endereco = form_doador.cleaned_data['endereco']
        cpf = form_doador.cleaned_data['cpf']
        telefone =form_doador.cleaned_data['telefone']
        data_nascimento= form_doador.cleaned_data['data_nascimento']
        peso =form_doador.cleaned_data['peso']
        cod_tiposang = form_doador.cleaned_data['cod_tiposang']
        novo_doador = Doador(nome=nome, endereco=endereco, cpf=cpf,telefone=telefone,
                                data_nascimento=data_nascimento, peso=peso,cod_tiposang=cod_tiposang)
        doador_service.editar_doador(doador_bd, novo_doador)
        return redirect('listar_doador')

    return render(request, 'doador/form_doador.html', {'form_doador': form_doador})


@login_required()
def excluir_doador(request, id):
    doador_bd = doador_service.listar_doador_id(id)
    if request.method == 'POST':
        doador_service.excluir_doador(doador_bd)
        return redirect('listar_doador')
    return render(request, 'doador/confirmar_exclusao_doador.html', {'doador': doador_bd})
