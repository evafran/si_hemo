from django.shortcuts import render,redirect
from ...forms import DoacaoForm
from ...entidades.doacao import Doacao
from ...services import doacao_service
from ...models import vw_historicoDoacao
from django.contrib.auth.decorators import login_required
from django.db import connection
from ...forms import DoacaoForm
from ...models import Agendamento, Doacao
from ...services import doacao_service

@login_required()
def inserir_doacao(request):
    if request.method == 'POST':
        form_doacao = DoacaoForm(request.POST)
        if form_doacao.is_valid():
            cod_agen = form_doacao.cleaned_data['cod_agen']
            cod_func = form_doacao.cleaned_data['cod_func']
            data_hora = form_doacao.cleaned_data['data_hora']

            # Obter o agendamento para acessar o doador e, em seguida, o tipo de sangue
            agendamento = Agendamento.objects.get(id=cod_agen.id)
            id_tipo_sangue = agendamento.cod_doador.cod_tiposang.id

            # Chamar a procedure para atualizar o estoque
            sucesso = atualizar_estoque(id_tipo_sangue, 1)  # A quantidade doada é -1 para diminuir o estoque

            if sucesso:
                nova_doacao = Doacao(cod_agen=cod_agen, cod_func=cod_func, data_hora=data_hora)
                doacao_service.inserir_doacao(nova_doacao)
                return redirect('listar_agendamentos')
    else:
        form_doacao = DoacaoForm()

    return render(request, 'doacao/form_doacao.html', {'form_doacao': form_doacao})

def atualizar_estoque(id_tipo_sangue, quantidade_modificada):
    with connection.cursor() as cursor:
        cursor.execute("CALL AtualizarEstoque(%s, %s, @sucesso)", [id_tipo_sangue, quantidade_modificada])
        cursor.execute("SELECT @sucesso")
        sucesso = cursor.fetchone()[0]
        return sucesso

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

@login_required()
def historico(request):
    nome_query = request.GET.get('nome')
    if nome_query:
        resultados = vw_historicoDoacao.objects.filter(nome__icontains=nome_query)
    else:
        resultados = vw_historicoDoacao.objects.none()
    return render(request,'doacao/historico_doacao.html',{'resultados': resultados})