from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ...forms import FuncionarioForm


def cadastrar_usuario(request):
    if request.method == 'POST':
        # form padrão do django para cadastro e login de usuários
        form_usuario = UserCreationForm(request.POST)
        form_funcionario = FuncionarioForm(request.POST)
        if form_usuario.is_valid() and form_funcionario.is_valid():
            # salva usuário
            user=form_usuario.save()

            # cria uma instância de funcionário assosciada ao usuário

            funcionario = form_funcionario.save(commit=False)
            funcionario.usuario = user
            funcionario.save()


            return redirect('listar_agendamentos')
    else:
        form_usuario = UserCreationForm()
        form_funcionario = FuncionarioForm()

    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario, 'form_funcionario': form_funcionario})


def logar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciais de usuário inválidas')
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form_login': form_login})


def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')


