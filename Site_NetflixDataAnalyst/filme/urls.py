from django.urls import path, reverse_lazy
from .views import Homepage, Homefilmes, Detalhesfilme, Pesquisafilme, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view

app_name = 'filme'

# Configuração das URLS (urlpatterns = padrões de url)
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    # Informa o caminho da urls das páginas dos "filmes" > http://Site/
    # conectando com classe que gerencia a página html Homepage
    # name='homepage' significa que “homepage” será a variavel do caminho da (URL) que será utilizada nas páginas
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    # Informa o caminho da urls das páginas dos "filmes" após estar logado > http://Site/filmes
    # conectando com classe que gerencia a página html Homefilmes
    # name='homefilmes' significa que “homefilmes” será a variavel do caminho da (URL) que será utilizada nas páginas
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
    # Informa o caminho da urls das páginas dos "filmes" após estar logado
    # conectando com classe que gerencia a página html Detalhesfilme
    # identificando com o ID qual deseja acessar > http://Site/filmes/id(Chave primária)
    # name='detalhesfilme' significa que “detalhesfilme” será a variavel do caminho da (URL) que será utilizada nas pág.
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme'),
    # Informa o caminho da url da página de pesquisa dos "filmes" > http://Site/pesquisa/
    # conectando com classe que gerencia a página html pesquisafilme
    # name='pesquisafilme' significa que “pesquisafilme” será a variavel do caminho da (URL) que será utilizada nas pág.
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    # Informa o caminho da url da página de login > http://Site/login/
    # Na biblioteca do Django existe a classe do login (auth_view . LoginView), por tanto não precisa cria-la na view
    # É necessário colocar o nome da página que controla no parâmetro, pois possuem o mesmo módulo "criador" auth_view
    # name='login' significa que “login” será a variavel do caminho da (URL) que será utilizada nas páginas
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # Informa o caminho da url da página de logout > http://Site/logout/
    # Na biblioteca do Django existe a classe do logout (auth_view . LogoutView), por tanto não precisa cria-la na view
    # É necessário colocar o nome da página que controla no parâmetro, pois possuem o mesmo módulo "criador" auth_view
    # name='logout' significa que “logout” será a variavel do caminho da (URL) que será utilizada nas páginas
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    # Informa o caminho da url da página de editar perfil após estar logado > http://Site/editarperfil/
    # conectando com classe que gerencia a página html Paginaperfil
    # name='editarperfil' significa que “editarperfil” será a variavel do caminho da (URL) que será utilizada nas pág.
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    # Informa o caminho da url da página de editar perfil após estar logado > http://Site/editarperfil/
    # conectando com classe que gerencia a página html Paginaperfil
    # name='criarconta' significa que “criarconta” será a variavel do caminho da (URL) que será utilizada nas pág.
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('filme:homefilmes')),
         name='mudarsenha')
]
# Informa o caminho da url de mudança de senha após estar logado, utilizando a página editarperfil como base
# (template_name='editarperfil.html') > http://Site/mudarsenha/
# Na biblioteca do Django existe a classe de edição de senha (auth_view . PasswordChangeView)
# por tanto não precisa cria-la na view.
# A success_url verifica se todos os campos do formulario foram preenchidos com sucesso
# Caso positivo, retornará um link que corresponde ao homefilmes
# name='mudarsenha' significa que “mudarsenha” será a variavel do caminho da (URL) que será utilizada nas pág.
