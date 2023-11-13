from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ...models import Funcionario  


def home(request):
    return render(request, 'home/home.html')


#acessa o nome do usuário que está logado 
@login_required
def home(request):
    try:
        funcionario = Funcionario.objects.get(usuario=request.user)
        nome_do_usuario = f"{funcionario.nome}"
    except Funcionario.DoesNotExist:
        nome_do_usuario = "Nome do Usuário não encontrado"

    return render(request, 'home/home.html', {'nome_do_usuario': nome_do_usuario})
