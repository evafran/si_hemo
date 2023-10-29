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
