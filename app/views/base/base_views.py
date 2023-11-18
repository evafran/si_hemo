from django.shortcuts import render
from ...services import funcionario_service
from django.contrib.auth.decorators import login_required


@login_required()
def listar_funcionario_base(request):
    funcionario = funcionario_service.listar_funcionario(request.user)
    return render(request, 'funcionario/listar_funcionario.html', {'funcionario': funcionario})