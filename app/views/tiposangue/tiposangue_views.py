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
