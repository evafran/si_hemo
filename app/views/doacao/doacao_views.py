from django.shortcuts import render,redirect
from ...forms import DoacaoForm
from ...entidades.doacao import Doacao
from ...services import doacao_service
from django.contrib.auth.decorators import login_required

@login_required()

def inserir_doacao(request):
    if request.method == 'POST':
        # se o método for == POST, vai passar os dados da requisição para o formulário
        form_doacao= DoacaoForm(request.POST)
        if form_doacao.is_valid():
            # captura as infos que vieram do formulário
            cod_agen = form_doacao.cleaned_data['cod_agen']
            cod_func = form_doacao.cleaned_data['cod_func']
            data_hora = form_doacao.cleaned_data['data_hora']
            
            
            nova_doacao = Doacao(cod_agen=cod_agen, cod_func=cod_func, data_hora=data_hora)
            # envia o objeto com os dados para o hospital_service, que insere no BD
            doacao_service.inserir_doacao(nova_doacao)
            return redirect('listar_agendamentos')
    else:
        # cria uma instância vazia do formulário caso o método não seja POST
        form_doacao = DoacaoForm()
    return render(request, 'doacao/form_doacao.html', {'form_doacao': form_doacao})

# com login_required exibe o método apenas se o usuário estiver logado, se não, redireciona para página de login
@login_required()
def listar_doacao(request):
    doacao = doacao_service.listar_doacao(request.user)
    return render(request, 'doacao/listar_doacao.html', {'doacao': doacao})

@login_required()
def editar_doacao(request,id):
    # armazena o doacao que o usuário está buscando através do tipo
    doacao_bd = doacao_service.listar_doacao_id(id)
    # aviso caso o usuário tente editar um doacao que ele nao tem acesso, através da url
    form_doacao= DoacaoForm(request.POST or None, instance=doacao_bd)
    if form_doacao.is_valid():
        cod_agen = form_doacao.cleaned_data['cod_agen']
        cod_func = form_doacao.cleaned_data['cod_func']
        data_hora= form_doacao.cleaned_data['data_hora']

        novo_doacao = Doacao( cod_agen= cod_agen, cod_func=cod_func, data_hora=data_hora)
        doacao_service.editar_doacao(doacao_bd, novo_doacao)
        return redirect('listar_doacao')

    return render(request, 'doacao/form_doacao.html', {'form_doacao': form_doacao})


@login_required()
def excluir_doacao(request, id):
    doacao_bd = doacao_service.listar_doacao_id(id)
    if request.method == 'POST':
        doacao_service.excluir_doacao(doacao_bd)
        return redirect('listar_doacao')
    return render(request, 'doacao/confirmar_exclusao_doacao.html', {'doacao': doacao_bd})