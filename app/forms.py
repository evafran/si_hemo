# faz as validações antes de inserir no bd e cria o formulário de cadastro de uma classe
from django import forms
from .models import TipoSangue, Hospital, Funcionario, Dispersao, Doador, Agendamento, Doacao

# Formulário para TipoSangue
class TipoSangueForm(forms.ModelForm):
    class Meta:
        model = TipoSangue
        fields = '__all__'

# Formulário para Hospital
class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

# Formulário para Funcionario
class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        exclude = ('usuario', )
        # todos os campos do models serão validados, exceto o que foi passado no exclude
        fields = '__all__'

# Formulário para Dispersao
class DispersaoForm(forms.ModelForm):
    class Meta:
        model = Dispersao
        fields = '__all__'