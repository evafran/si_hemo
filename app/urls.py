from django.urls import path
from .views.lembrete_views import *
from .views.funcionario.usuario_views import *
from .views.doador.doador_views import *
from .views.agendamento.agendamento_views import *
from .views.tiposangue.tiposangue_views import *
from.views.hospital.hospital_views import *
from.views.dispersao.dispersao_views import *
from.views.doacao.doacao_views import *
from.views.home.home_views import *
from.views.tela_descanso_home.tela_descanso_home_views import *

urlpatterns = [
    path('', tela_descanso_home, name='tela_descanso_home'),
    path('home',home, name='home'),
    path('listar_agendamentos',listar_agendamentos,name='listar_agendamentos'),
    path('listar_doador',listar_doador,name='listar_doador'),
    path('listar_hospital',listar_hospital,name='listar_hospital'),
    path('listar_tiposangue',listar_tiposangue,name='listar_tiposangue'),
    path('editar_tiposangue/<int:id>',editar_tiposangue,name='editar_tiposangue'),
    path('excluir_tiposangue/<int:id>',excluir_tiposangue,name='excluir_tiposangue'),
    path('cadastrar_doador',cadastrar_doador,name='cadastrar_doador'),
    path('cadastrar_tiposangue',cadastrar_tiposangue,name='cadastrar_tiposangue'),
    path('cadastrar_hospital',cadastrar_hospital,name='cadastrar_hospital'),
    path('editar_hospital/<int:id>',editar_hospital,name='editar_hospital'),
    path('excluir_hospital/<int:id>',excluir_hospital,name='excluir_hospital'),
    path('solicitar_dispersao',solicitar_dispersao,name='solicitar_dispersao'),
    path('listar_dispersao',listar_dispersao,name='listar_dispersao'),
    path('editar_dispersao/<int:id>',editar_dispersao,name='editar_dispersao'),
    path('excluir_dispersao/<int:id>',excluir_dispersao,name='excluir_dispersao'),
    path('inserir_doacao',inserir_doacao,name='inserir_doacao'),
    path('listar_doacao',listar_doacao,name='listar_doacao'),
    path('editar_doacao/<int:id>',editar_doacao,name='editar_doacao'),
    path('excluir_doacao/<int:id>',excluir_doacao,name='excluir_doacao'),
    path('cadastrar_agendamento',cadastrar_agendamento,name='cadastrar_agendamento'),
    path('editar_agendamento/<int:id>', editar_agendamento, name='editar_agendamento'),
    path('excluir_agendamento/<int:id>', excluir_agendamento, name='excluir_agendamento'),
    path('editar_doador/<int:id>', editar_doador, name='editar_doador'),
    path('excluir_doador/<int:id>', excluir_doador, name='excluir_doador'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario')
]
