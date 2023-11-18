from django.shortcuts import render
from django.shortcuts import render

def tela_home(request):
    return render(request, 'home/home.html')