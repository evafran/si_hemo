from django.shortcuts import render,redirect
from ...forms import TipoSangueForm
from ...entidades.tiposangue import TipoSangue
from ...services import tiposangue_service
from django.contrib.auth.decorators import login_required

@login_required()

def cadastrar_tiposangue(request):
    if request.method == 'POST':
        # se o método for == POST, vai passar os dados da requisição para o formulário
        form_tiposangue= TipoSangueForm(request.POST)
        if form_tiposangue.is_valid():
            # captura as infos que vieram do formulário
            tipo = form_tiposangue.cleaned_data['tipo']
            quantidade = form_tiposangue.cleaned_data['quantidade']


            novo_tiposangue = TipoSangue(tipo=tipo, quantidade=quantidade)
            # envia o objeto com os dados para o tiposangue_service, que insere no BD
            tiposangue_service.cadastrar_tiposangue(novo_tiposangue)
            return redirect('listar_agendamentos')
    else:
        # cria uma instância vazia do formulário caso o método não seja POST
        form_tiposangue = TipoSangueForm()
    return render(request, 'tiposangue/form_tiposangue.html', {'form_tiposangue': form_tiposangue})


# com login_required exibe o método apenas se o usuário estiver logado, se não, redireciona para página de login
@login_required()
def listar_tiposangue(request):
    tiposangue = tiposangue_service.listar_tiposangue(request.user)
    return render(request, 'tiposangue/listar_tiposangue.html', {'tiposangue': tiposangue})

@login_required()
def editar_tiposangue(request,id):
    # armazena o tiposangue que o usuário está buscando através do tipo
    tiposangue_bd = tiposangue_service.listar_tiposangue_id(id)
    # aviso caso o usuário tente editar um tiposangue que ele nao tem acesso, através da url
    form_tiposangue= TipoSangueForm(request.POST or None, instance=tiposangue_bd)
    if form_tiposangue.is_valid():
        tipo = form_tiposangue.cleaned_data['tipo']
        quantidade= form_tiposangue.cleaned_data['quantidade']

        novo_tiposangue = TipoSangue( tipo= tipo, quantidade=quantidade)
        tiposangue_service.editar_tiposangue(tiposangue_bd, novo_tiposangue)
        return redirect('listar_tiposangue')

    return render(request, 'tiposangue/form_tiposangue.html', {'form_tiposangue': form_tiposangue})


@login_required()
def excluir_tiposangue(request, id):
    tiposangue_bd = tiposangue_service.listar_tiposangue_id(id)
    if request.method == 'POST':
        tiposangue_service.excluir_tiposangue(tiposangue_bd)
        return redirect('listar_tiposangue')
    return render(request, 'tiposangue/confirmar_exclusao_tiposangue.html', {'tiposangue': tiposangue_bd})