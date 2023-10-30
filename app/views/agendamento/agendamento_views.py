from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from ...entidades.agendamento import Agendamento
from ...services import agendamento_service
from ...forms import AgendamentoForm

@login_required()

def listar_agendamentos(request):
    agendamentos = agendamento_service.listar_agendamentos(request.user)
    return render(request,'agendamento/listar_agendamentos.html',{'agendamentos':agendamentos})

@login_required
def cadastrar_agendamento(request):
    if request.method=='POST':
        form_agendamento = AgendamentoForm(request.POST)
        if form_agendamento.is_valid():
            cod_doador=form_agendamento.cleaned_data['cod_doador']
            data_hora=form_agendamento.cleaned_data['data_hora']
            novo_agendamento =Agendamento(cod_doador=cod_doador,data_hora=data_hora)
            agendamento_service.cadastrar_agendamento(novo_agendamento)
            
            return redirect('listar_agendamentos')
    else:
        form_agendamento=AgendamentoForm()
    return render(request,'agendamento/form_agendamento.html',{'form_agendamento':form_agendamento})


@login_required()
def editar_agendamento(request, id):
    # armazena o agendamento que o usuário está buscando através do id
    agendamento_bd= agendamento_service.listar_agendamento_id(id)
    # aviso caso o usuário tente editar um agendamentoque ele nao tem acesso, através da url
    #if agendamento_bd.usuario != request.user:
        #return HttpResponse('Não permitido')
    form_agendamento = AgendamentoForm(request.POST or None, instance=agendamento_bd)
    if form_agendamento.is_valid():
        cod_doador = form_agendamento.cleaned_data['cod_doador']
        data_hora = form_agendamento.cleaned_data['data_hora']
        novo_agendamento = Agendamento(cod_doador=cod_doador, data_hora=data_hora)
        agendamento_service.editar_agendamento(agendamento_bd, novo_agendamento)
        return redirect('listar_agendamentos')

    return render(request, 'agendamento/form_agendamento.html', {'form_agendamento': form_agendamento})


@login_required()
def excluir_agendamento(request, id):
    agendamento_bd= agendamento_service.listar_agendamento_id(id)
    #if agendamento_bd.usuario != request.user:
        #return HttpResponse('Não permitido')
    if request.method == 'POST':
        agendamento_service.excluir_agendamento(agendamento_bd)
        return redirect('listar_agendamentos')
    return render(request, 'agendamento/confirmar_exclusao_agendamento.html', {'agendamento': agendamento_bd})
