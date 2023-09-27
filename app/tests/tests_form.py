from django.test import TestCase
from ..forms import LembreteForm


class LembreteFormTestCase(TestCase):

    # verificar se um formulário com dados é válido
    def test_lembrete_form_valido(self):
        form = LembreteForm(data={
            'titulo': 'lembrete999',
            'descricao': 'lembrete para testes',
            'data': '2022-10-21',
            'prioridade': 'A'
        })
        self.assertTrue(form.is_valid())

    # verificar se formulário vazio é inválido
    def test_lembrete_form_invalido(self):
        form = LembreteForm(data={})
        self.assertFalse(form.is_valid())
