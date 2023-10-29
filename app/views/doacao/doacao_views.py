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
