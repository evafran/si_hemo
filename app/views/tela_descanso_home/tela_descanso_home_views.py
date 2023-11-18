from django.shortcuts import render
from django.shortcuts import render
 


def tela_descanso_home(request):
    return render(request, 'Home_descanso/tela_descanso.html')

