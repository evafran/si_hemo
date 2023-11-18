from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ...forms import FuncionarioForm
from ...services import funcionario_service
from django.contrib.auth.decorators import login_required
from ...entidades.funcionario import Funcionario


def cadastrar_funcionario(request):
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)
        form_funcionario = FuncionarioForm(request.POST)
        if form_usuario.is_valid() and form_funcionario.is_valid():
            # Salva o usuário, mas não comita ainda
            user = form_usuario.save(commit=False)
            
            # Define o first_name do usuário com base no campo nome do funcionário
            user.first_name = form_funcionario.cleaned_data['nome']
            
            # Agora, salva o usuário com o first_name atualizado
            user.save()

            # Cria uma instância de funcionário associada ao usuário
            funcionario = form_funcionario.save(commit=False)
            funcionario.usuario = user
            funcionario.save()

            return redirect('listar_agendamentos')
    else:
        form_usuario = UserCreationForm()
        form_funcionario = FuncionarioForm()

    return render(request, 'funcionario/form_funcionario.html', {'form_usuario': form_usuario, 'form_funcionario': form_funcionario})


def logar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_agendamentos')
        else:
            messages.error(request, 'Credenciais de usuário inválidas')
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'funcionario/login.html', {'form_login': form_login})


def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')



# com login_required exibe o método apenas se o usuário estiver logado, se não, redireciona para página de login
@login_required()
def listar_funcionario(request):
    funcionario = funcionario_service.listar_funcionario(request.user)
    return render(request, 'funcionario/listar_funcionario.html', {'funcionario': funcionario})



@login_required()
def editar_funcionario(request, id):
    # armazena o funcionario que o usuário está buscando através do id
    funcionario_bd = funcionario_service.listar_funcionario_id(id)
    # aviso caso o usuário tente editar um funcionario que ele nao tem acesso, através da url
    form_funcionario = FuncionarioForm(request.POST or None, instance=funcionario_bd)
    if form_funcionario.is_valid():
        nome = form_funcionario.cleaned_data['nome']
        cpf = form_funcionario.cleaned_data['cpf']
        endereco = form_funcionario.cleaned_data['endereco']
        telefone =form_funcionario.cleaned_data['telefone']
        usuario= form_funcionario.cleaned_data['usuario']
        novo_funcionario = Funcionario(nome=nome, cpf=cpf, endereco=endereco,telefone=telefone,
                                usuario=usuario)
        funcionario_service.editar_funcionario(funcionario_bd, novo_funcionario)
        return redirect('listar_funcionario')

    return render(request, 'funcionario/form_funcionario.html', {'form_funcionario': form_funcionario})


@login_required()
def excluir_funcionario(request, id):
    funcionario_bd = funcionario_service.listar_funcionario_id(id)
    if request.method == 'POST':
        funcionario_service.excluir_funcionario(funcionario_bd)
        return redirect('listar_funcionario')
    return render(request, 'funcionario/confirmar_exclusao_funcionario.html', {'funcionario': funcionario_bd})
