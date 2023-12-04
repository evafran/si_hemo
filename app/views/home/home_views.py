from django.shortcuts import render
from django.shortcuts import render
from ...certificado.cert_required import cert_required
from django.views.decorators.csrf import csrf_exempt  # Use isso se a visualização não exigir CSRF (em alguns casos de POST, por exemplo) 





@cert_required
def tela_home(request):
    return render(request, 'home/home.html')



