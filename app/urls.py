from django.urls import path
from .views.lembrete_views import *
from .views.usuario_views import *

urlpatterns = [
    path('', listar_lembretes, name='listar_lembretes'),
    path('cadastrar_lembrete/', cadastrar_lembrete, name='cadastrar_lembrete'),
    path('editar_lembrete/<int:id>', editar_lembrete, name='editar_lembrete'),
    path('excluir_lembrete/<int:id>', excluir_lembrete, name='excluir_lembrete'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario')
]
