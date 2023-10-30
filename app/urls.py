from django.urls import path
from .views.lembrete_views import *
from .views.funcionario.usuario_views import *
from .views.doador.doador_views import *
from .views.agendamento.agendamento_views import *
from .views.tiposangue.tiposangue_views import *
from.views.hospital.hospital_views import *
from.views.dispersao.dispersao_views import *
from.views.doacao.doacao_views import *


urlpatterns = [
    path('',listar_agendamentos,name='listar_agendamentos'),
    path('listar_doador',listar_doador,name='listar_doador'),
    path('cadastrar_doador',cadastrar_doador,name='cadastrar_doador'),
    path('cadastrar_tiposangue',cadastrar_tiposangue,name='cadastrar_tiposangue'),
    path('cadastrar_hospital',cadastrar_hospital,name='cadastrar_hospital'),
    path('solicitar_dispersao',solicitar_dispersao,name='solicitar_dispersao'),
    path('inserir_doacao',inserir_doacao,name='inserir_doacao'),
    path('cadastrar_agendamento',cadastrar_agendamento,name='cadastrar_agendamento'),
    path('editar_agendamento/<int:id>', editar_agendamento, name='editar_agendamento'),
    path('excluir_agendamento/<int:id>', excluir_agendamento, name='excluir_agendamento'),
    path('editar_doador/<int:id>', editar_doador, name='editar_doador'),
    path('excluir_doador/<int:id>', excluir_doador, name='excluir_doador'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario')
]
