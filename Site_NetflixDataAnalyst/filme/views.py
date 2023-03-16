from .models import Filme, Usuario
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from .forms import CriarContaForm, FormHomepage


class Homepage(FormView):
    # Era class Homepage(TemplateView):
    # A classe Homepage (TemplateView) possui uma estrutura definida pelo django
    # Ela obrigatoriamente exige a criação da variável template_name
    # A variável template_name realiza a solicitação dos conteudos da página “homepage”
    template_name = "homepage.html"
    # Ela obrigatoriamente exige a criação da variável form_class
    # A variável form_class realiza a conexão do formulário criado com a classe
    # criando um formulario com todos os atributos/métodos da classe FormHomepage
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        # Se o usuario estiver autenticado
        if request.user.is_authenticated:
            # Redirecionando o usuario para a URL Homefilmes
            return redirect('filme:homefilmes')
        # Caso contrário
        else:
            # Redirecionando o usuario para a URL Homepage
            return super(Homepage, self).get(request, *args, **kwargs)

    def get_success_url(self):
        # A função verifica se todos os campos do formulario foram preenchidos com sucesso
        # Caso positivo, armazenará na variavel email:
        # A variavel email será uma requisição que pegará o parâmetro contido no campo email
        email = self.request.POST.get('email')
        # Armazene no lista_usuarios o filtro/busca o email digitado contido na coluna email do objeto Usuario
        lista_usuarios = Usuario.objects.filter(email=email)
        # Se o email do usuario estiver contido na lista_usuarios então:
        if lista_usuarios:
            # Redirecionando o usuario para a URL login
            return reverse('filme:login')
        # Caso contrário
        else:
            # Redirecionando o usuario para a URL criarconta
            return reverse('filme:criarconta')


class Homefilmes(LoginRequiredMixin, ListView):
    # A classe Homefilmes (ListView) possui uma estrutura definida pelo django
    # Ela obrigatoriamente exige a criação da variável template_name
    # A variável template_name realiza a solicitação dos conteudos da página homefilmes
    template_name = "homefilmes.html"
    # Ela obrigatoriamente exige a criação da variável model
    # A variável model realiza a conexão do BACK-END e FRONT-END,
    # criando uma lista de objetos/filmes (object_list) com todos os atributos/métodos da classe Filme
    model = Filme


class Detalhesfilme(LoginRequiredMixin, DetailView):
    # A classe Detalhesfilme (DetailView) possui uma estrutura definida pelo django
    # Ela obrigatoriamente exige a criação da variável template_name
    # A variável template_name realiza a solicitação dos conteudos da página homefilmes
    template_name = 'detalhesfilme.html'
    # Ela obrigatoriamente exige a criação da variável model
    # A variável model realiza a conexão do BACK-END e FRONT-END,
    # criando uma apenas um objeto/filme (object) com todos os atributos/métodos da classe Filme
    model = Filme

    def get(self, request, *args, **kwargs):
        # Descobrir qual o filme é acessado
        filme = self.get_object()
        # Somar 1 nas visualizações daquele filme
        filme.visualizacao += 1
        # Salvar a quantidade
        filme.save()
        # Armazena na variável o usuario que está logado pela requisição feita
        usuario = request.user
        # Neste usuario será adicionado na coluna Filmes_vistos o filme acessado
        usuario.filmes_vistos.add(filme)
        # Redirecionando o usuario para a URL final
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # A função get_context_data possui uma estrutura definida pelo django
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # Filtrar a tabela Filme pegando os filmes cuja categoria é igual a categoria do filme atual (object)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context


class Pesquisafilme(LoginRequiredMixin, ListView):
    # A classe Pesquisafilme (ListView) possui uma estrutura definida pelo django
    # Ela obrigatoriamente exige a criação da variável template_name
    # A variável template_name realiza a solicitação dos conteudos da página pesquisa
    template_name = 'pesquisa.html'
    # Ela obrigatoriamente exige a criação da variável model
    # A variável model realiza a conexão do BACK-END e FRONT-END,
    # criando uma lista de objetos/filmes (object_list) com todos os atributos/métodos da classe Filme
    model = Filme

    def get_queryset(self):
        # A função get_queryset possui uma estrutura definida pelo django
        # O termo de pesquisa será uma requisição que pegará o parâmetro contido na query
        termo_pesquisa = self.request.GET.get('query')
        # Se existir o termo de pesquisa, ou seja, um parametro contido na query
        if termo_pesquisa:
            # Armazene no object_list o filtro/busca do título contido no termo pesquisa do objeto Filme
            object_list = self.model.objects.filter(titulo_icontains=termo_pesquisa)
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, UpdateView):
    # De: class Paginaperfil(LoginRequiredMixin, TemplateView) para class Paginaperfil(LoginRequiredMixin, UpdateView)
    # A classe Paginaperfil (TemplateView) possui uma estrutura definida pelo django
    # Ela obrigatoriamente exige a criação da variável template_name
    # A variável template_name realiza a solicitação dos conteudos da página editarperfil
    template_name = "editarperfil.html"
    # Ela obrigatoriamente exige a criação da variável model
    # A variável model realiza a conexão do BACK-END e FRONT-END com todos os atributos/métodos da classe Usuario
    model = Usuario
    # fields é uma lista das colunas que serão atualizados do modelo Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        # A função verifica se todos os campos do formulario foram preenchidos com sucesso
        # Caso positivo, retornará um link que corresponde ao homefilmes
        return reverse('filme:homefilmes')


class Criarconta(FormView):
    # A classe Criarconta (FormView) possui uma estrutura definida pelo django
    # Ela obrigatoriamente exige a criação da variável template_name
    # A variável template_name realiza a solicitação dos conteudos da página criarconta
    template_name = "criarconta.html"
    # Ela obrigatoriamente exige a criação da variável form_class
    # A variável form_class realiza a conexão do formulário criado com a classe
    # criando um formulario com todos os atributos/métodos da classe CriarContaForm
    form_class = CriarContaForm

    def form_valid(self, form):
        # A função valida, conforme as regras, todos os campos do formulario e salva as informações no banco de dados,
        # pois criamos um usuario no banco de dados
        form.save()
        # Redirecionando o usuario para a URL Criarconta
        return super(Criarconta, self).form_valid(form)

    def get_success_url(self):
        # A função verifica se todos os campos do formulario foram preenchidos com sucesso
        # Caso positivo, retornará um link que corresponde ao login
        return reverse('filme:login')
