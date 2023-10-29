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