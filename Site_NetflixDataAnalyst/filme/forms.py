from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class FormHomepage(forms.Form):
    # Criação do campo e-mail, pois não vem na estrutura do Django
    # label = False significa que não vai aparecer o rótulo(texto email) na página HTML¶
    email = forms.EmailField(label=False)


class CriarContaForm(UserCreationForm):
    # Criação do campo e-mail, pois não vem na estrutura do Django
    email = forms.EmailField()

    # A classe Meta é uma classe padronizada do Django
    class Meta:
        # Usando a tabela/modelo Usuario como base para a criação do formulário
        model = Usuario
        # Os campos obritários do formulário serão: Nome, e-mail, senha e confirmação de senha
        fields = ('username', 'email', 'password1', 'password2')
