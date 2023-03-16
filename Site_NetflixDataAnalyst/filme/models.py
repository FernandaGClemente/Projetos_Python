from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Lista constante com os nomes das categorias dos "Filmes"
LISTA_CATEGORIAS = (
    # Nome que constará na tabela do banco de dados e Nome que será exibido para o usuário
    ('ANALISES', 'Análises'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'Outros'),
)


#  Criação da Tabela Filme
class Filme(models.Model):
    # Coluna Título terá um campo de caracteres com um comprimento máximo de 100
    titulo = models.CharField(max_length=100)
    # Coluna Thumb terá um campo de Imagem onde os utilizadores enviaram a imagem para a pasta "thumb_filmes"
    thumb = models.ImageField(upload_to='thumb_filmes')
    # Coluna Descrição terá um campo de texto com um comprimento máximo de 1000
    descricao = models.TextField(max_length=1000)
    # Coluna Categoria terá um campo de caracteres com um comprimento máximo de 15 e
    # receberá como escolha de categorias uma lista constante dos "Filmes"
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    # Coluna Cisualização terá um campo inteiro com um valor padrão = 0
    visualizacao = models.IntegerField(default=0)
    # Coluna Data da criação terá um campo de data e hora com um valor padrão = fuso horário de agora
    data_criacao = models.DateTimeField(default=timezone.now)

    # Criação da função String
    def __str__(self):
        # Objetivo é fazer com que todos os objetos Strings da classe Filme
        # tenham os mesmos atributos do título
        return self.titulo


#  Criação da Tabela Episodio
class Episodio(models.Model):
    # Coluna Filme terá um campo de Chave estrangeira que conecta com o ID (Chave primaria) da tabela Filme
    # related_name='episodios' > Relaciona os nomes dos episódios com a Tabela Filme
    # on_delete=models.CASCADE > Caso o filme seja excluído os episódios tambem serão, num efeito cascada
    filme = models.ForeignKey("Filme", related_name='episodios', on_delete=models.CASCADE)
    # Coluna Título terá um campo de caracteres com um comprimento máximo de 100
    titulo = models.CharField(max_length=100)
    # Coluna Vídeo terá um campo de url
    video = models.URLField()

    # Criação da função String
    def __str__(self):
        # Objetivo é fazer com que todos os objetos Strings da classe Episodio
        # tenham os mesmos atributos do título mais o nome do título do filme
        return self.filme.titulo + " - " + self.titulo


#  Criação da Tabela Usuario
class Usuario(AbstractUser):
    # As variáveis nome, sobrenome, e-mail, etc. já existem e possui uma estrutura definida pelo django
    # Devemos criar apenas as colunas que não existem nessa estrutura
    # Coluna Filmes_vistos terá um campo "muitos para muitos" onde se relacionará com a classe Filme
    filmes_vistos = models.ManyToManyField('Filme')
