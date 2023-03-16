from .models import Filme


def lista_filmes_novos(request):
    # Filme.objects.all() = Lista de todos os filmes
    # order_by('-data_criacao') = Lista ordenada pela data de criação do filme, do mais novo para o mais antigo (Menos)
    # [0:8] = Só mostrará os 8 primeiros filmes da lista
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    # Se existir a lista de filmes então:
    if lista_filmes:
        # Armazene na variável o primeiro filmes da lista
        filme_destaque = lista_filmes[0]
    else:
        # Caso contrario, armazene nada
        filme_destaque = None
    # 'Lista_filmes_novos': lista_filmes = Está armazendo no valor do dict a lista de filmes
    # 'Filme_destaque': filme_destaque = Está armazendo no valor do dict apenas o primeiro filme.
    # Filme_destaque e Lista_filmes_novos serão usadas nas páginas em HTML
    return {'lista_filmes_novos': lista_filmes, 'filme_destaque': filme_destaque}


def lista_filmes_populares(request):
    # Filme.objects.all() = Lista de todos os filmes
    # order_by('-visualizacao') = Lista ordenada pela quantidade de visualizacao, do maior para o menor (Menos)
    # [0:8] = Só mostrará os 8 primeiros filmes da lista
    # 'lista_filmes_populares': lista_filmes = Está armazendo no valor do dict a lista de filmes
    # Que poderá ser usada nas páginas em HTML
    lista_filmes = Filme.objects.all().order_by('-visualizacao')[0:8]
    return {'lista_filmes_populares': lista_filmes}
