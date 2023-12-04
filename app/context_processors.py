from .services import funcionario_service

def funcionario_context(request):
    funcionario_validacao = funcionario_service.listar_funcionario(request.user) if request.user.is_authenticated else None
    return {'funcionario_validacao': funcionario_validacao}