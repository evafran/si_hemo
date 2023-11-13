from django.shortcuts import render,redirect
from ...forms import DispersaoForm
from ...entidades.dispersao import Dispersao
from ...services import dispersao_service
from django.contrib.auth.decorators import login_required

@login_required()

def solicitar_dispersao(request):
    if request.method == 'POST':
        # se o método for == POST, vai passar os dados da requisição para o formulário
        form_dispersao= DispersaoForm(request.POST)
        if form_dispersao.is_valid():
            # captura as infos que vieram do formulário
            cod_func = form_dispersao.cleaned_data['cod_func']
            cod_hospital = form_dispersao.cleaned_data['cod_hospital']
            cod_tiposang = form_dispersao.cleaned_data['cod_tiposang']
            qtd_bolsa = form_dispersao.cleaned_data['qtd_bolsa']
            data = form_dispersao.cleaned_data['data']
            nova_dispersao = Dispersao(cod_func=cod_func, cod_hospital=cod_hospital, cod_tiposang=cod_tiposang,qtd_bolsa=qtd_bolsa,data=data)
            # envia o objeto com os dados para o hospital_service, que insere no BD
            dispersao_service.solicitar_dispersao(nova_dispersao)
            return redirect('listar_agendamentos')
    else:
        # cria uma instância vazia do formulário caso o método não seja POST
        form_dispersao = DispersaoForm()
    return render(request, 'dispersao/form_dispersao.html', {'form_dispersao': form_dispersao})


# com login_required exibe o método apenas se o usuário estiver logado, se não, redireciona para página de login
@login_required()
def listar_dispersao(request):
    dispersao = dispersao_service.listar_dispersao(request.user)
    return render(request, 'dispersao/listar_dispersao.html', {'dispersao': dispersao})

@login_required()
def editar_dispersao(request,id):
    # armazena o dispersao que o usuário está buscando através do tipo
    dispersao_bd = dispersao_service.listar_dispersao_id(id)
    # aviso caso o usuário tente editar um dispersao que ele nao tem acesso, através da url
    form_dispersao= DispersaoForm(request.POST or None, instance=dispersao_bd)
    if form_dispersao.is_valid():
        cod_func = form_dispersao.cleaned_data['cod_func']
        cod_hospital = form_dispersao.cleaned_data['cod_hospital']
        cod_tiposang = form_dispersao.cleaned_data['cod_tiposang']
        qtd_bolsa = form_dispersao.cleaned_data['qtd_bolsa']
        data= form_dispersao.cleaned_data['data']

        novo_dispersao = Dispersao( cod_func= cod_func, cod_hospital=cod_hospital,cod_tiposang=cod_tiposang,qtd_bolsa=qtd_bolsa, data=data)
        dispersao_service.editar_dispersao(dispersao_bd, novo_dispersao)
        return redirect('listar_dispersao')

    return render(request, 'dispersao/form_dispersao.html', {'form_dispersao': form_dispersao})


@login_required()
def excluir_dispersao(request, id):
    dispersao_bd = dispersao_service.listar_dispersao_id(id)
    if request.method == 'POST':
        dispersao_service.excluir_dispersao(dispersao_bd)
        return redirect('listar_dispersao')
    return render(request, 'dispersao/confirmar_exclusao_dispersao.html', {'dispersao': dispersao_bd})