# faz as validações antes de inserir no bd e cria o formulário de cadastro de uma classe
from django import forms
from .models import *
from django.utils import timezone

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

#formulário para doador 
class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = '__all__'



#formulário para agendamento
class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = '__all__'
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }
    def clean_data_hora(self):
        data_hora=self.cleaned_data['data_hora']
        hora_atual= timezone.now()

        if data_hora < hora_atual:
            raise forms.ValidationError('Informe uma data válida ')
        return data_hora

        # Formulário para doaçaõ
class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = '__all__'
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }
    def clean_data_hora(self):
        data_hora=self.cleaned_data['data_hora']
        hora_atual= timezone.now()

        if data_hora <= hora_atual:
            raise forms.ValidationError('Informe uma data válida ')
        return data_hora