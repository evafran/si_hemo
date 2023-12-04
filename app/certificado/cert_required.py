from django.http import HttpResponseForbidden


def cert_required(view_func):
    def wrapped_view(request, *args, **kwargs): 
        if request.is_secure() and 'SSL_CLIENT_CERT' in request.META: # Verificar se o certificado é válido ou se contém informações específicas # Aqui você pode fazer verificações personalizadas no certificado, como a validação de informações 
            return view_func(request, *args, **kwargs) 
        else: 
            return view_func(request, *args, **kwargs) 
    return wrapped_view