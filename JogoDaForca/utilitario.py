import random
from constantes import DICT_NIVEIS_DIFICULDADE, DICT_TAMANHO_PALAVRAS


def exiba_menu_dificuldade():
    """
    Exibe o menu que permite o jogador selecionar o nível de dificuldade.

    Returns : Retorna o nível de dificuldade selecionado pelo utilizador. (ou)
    :return : String que representa o nível de dificuldade selecionado
    """

    print("A seguir escolha um nível de dificuldade:")

    v_configuracao_dificuldade = ""

    while not v_configuracao_dificuldade:
        for chave, valor in DICT_NIVEIS_DIFICULDADE.items():
            print(f"{chave} - {valor}")

        v_configuracao_dificuldade = input("Escolha a dificuldade pelo número associado: ")

        if v_configuracao_dificuldade not in DICT_NIVEIS_DIFICULDADE.keys():
            print(f"{v_configuracao_dificuldade} não é uma opção válida. Tente novamente!")
            v_configuracao_dificuldade = ""

    return v_configuracao_dificuldade


def escolha_palavra_aleatoria(v_configuracao_dificuldade):
    """
    Abre o arquivo que contém o banco de palavras e seleciona uma palavra
    aleatoriamente baseado no parâmetro v_configuracao_dificuldade

    :param v_configuracao_dificuldade : String que representa o nível de dificuldade.
    :return: String que representa a palavra aleatoriamente selecionada.
    """
    with open("static/words.txt", mode="r") as v_palavras:
        lista_palavras = []
        for v_palavra in v_palavras.readlines():

            v_palavra_sem_espaco = v_palavra.strip()
            tamanho_min, tamanho_max = DICT_TAMANHO_PALAVRAS[v_configuracao_dificuldade]
            if tamanho_min <= len(v_palavra_sem_espaco) <= tamanho_max:
                lista_palavras.append(v_palavra_sem_espaco)

    v_indice_maximo = len(lista_palavras) - 1
    v_indice_aleatorio = random.randint(a=0, b=v_indice_maximo)
    v_palavra_selecionada = lista_palavras[v_indice_aleatorio]
    print(v_palavra_selecionada)
    return v_palavra_selecionada


def obter_total_tentativas(v_palavra_selecionada, v_configuracao_dificuldade):
    """
    Obtem a quantidade de vezes que o jogador pode tentar adivinhar a palavra
    "v_palavra_selecionada" sem que o jogo chegue ao final.

    :param v_palavra_selecionada: "String" que representa a palavra aleatoriamente
    selecionada de dentro do banco de palavras.
    :param v_configuracao_dificuldade: "String" que representa o nível de dificuldade
    selecionado pelo utilizador.
    :return: Int. que representa o total de tentativas!
    """

    # Armazena na variavel um conjunto/set de letras da palavra escolhida aleatoriamente
    v_letras_unicas = set(v_palavra_selecionada)
    # Armazena na variavel a quantidade de letras desse conjunto e multiplica por 1,5
    v_total_tentativas = 1.5 * len(v_letras_unicas)
    # Armazena na variavel a quantidade de tentativas que o usuario terá, sendo:
    # Nivel de dificuldade igual a 1, o utilizador terá (1,5 x Tamanho das letras do conjunto) + 2
    # Nível de dificuldade igual a 2, o utilizador terá 1,5 x Tamanho das letras do conjunto
    # Nível de dificuldade igual a 3, o utilizador téra (1,5 x Tamanho das letras do conjunto) - 2, sendo que:
    # minimo será o total de tentativas calculdados anterior e o máximo é 18, independente da quantidade calculada
    if v_configuracao_dificuldade == "1":
        v_total_tentativas += 2
    elif v_configuracao_dificuldade == "3":
        v_total_tentativas -= 2
        v_total_tentativas = min([v_total_tentativas, 18])
    # Armazena na variavel a quantidade de tentativas arrendonda, resultando num número inteiro
    v_total_tentativas = round(v_total_tentativas)

    # print(f"A quantidade de tentativas para adivinha a palavra será de {v_total_tentativas}")
    return v_total_tentativas
