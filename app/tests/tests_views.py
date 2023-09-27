from django.test import TestCase
from django.urls import reverse


class UsuarioViewsTestCase(TestCase):

    # testes para verificar se os métodos da views estão retornando o código 200
    def test_status_code_200_cadastrar_usuario(self):
        response = self.client.get(reverse('cadastrar_usuario'))
        self.assertEqual(response.status_code, 200)

    def test_status_code_200_logar(self):
        response = self.client.get(reverse('logar_usuario'))
        self.assertEqual(response.status_code, 200)

    # testes para verificar se o template usado no método está renderizando a response
    def test_template_usado_cadastrar_usuario(self):
        response = self.client.get(reverse('cadastrar_usuario'))
        self.assertTemplateUsed(response, 'usuarios/form_usuario.html')

    def test_template_usado_logar(self):
        response = self.client.get(reverse('logar_usuario'))
        self.assertTemplateUsed(response, 'usuarios/login.html')
