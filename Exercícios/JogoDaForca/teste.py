import random

# Criação de um dicionário com as opções de níveis de dificuldade, assim eliminamos o bloco dos prints dentro do While
dict_niveis_dificuldade = {"1": "Nível Fácil", "2": "Nível Normal", "3": "Nível Difícil"}

# Criação de um dicionário com as opções de níveis de dificuldade agrupadas com a quantidade mínima e máxima
dict_tamanho_palavras = {"1": (3, 5), "2": (6, 10), "3": (11, 1000)}

print("A seguir escolha um nível de dificuldade:")

v_configuracao_dificuldade = ""

# Enquanto a variável estiver vazia (não conter valor), execute (Permaneça True)
while not v_configuracao_dificuldade:
    # print("1 - Nível Fácil")
    # print("2 - Nível Normal")
    # print("3 - Nível Dificil")
    # Para cada chave e valor no dicionário, mostre os seus itens
    for chave, valor in dict_niveis_dificuldade.items():
        print(f"{chave} - {valor}")

    v_configuracao_dificuldade = input("Escolha a dificuldade pelo número associado: ")

    # Se o valor inputado não estiver contido na chave do dicionario, mostre a mensagem e continue com a variavel vazia
    if v_configuracao_dificuldade not in dict_niveis_dificuldade.keys():
        print(f"{v_configuracao_dificuldade} não é uma opção válida. Tente novamente!")
        v_configuracao_dificuldade = ""

# print(v_configuracao_dificuldade)

# Comando que realiza a abertura do arquivo words.txt no modo de leitura (r) e armazena numa variavel
with open("static/words.txt", mode="r") as v_palavras:
    # print(v_palavras.readlines())  - Mostra todas as "palavras + \n" do arquivo words em linha
    lista_palavras = []  # Criação de uma lista vazia
    # Para cada palavra contida dentro do arquivo words
    for v_palavra in v_palavras.readlines():
        # lista_palavras.append(v_palavra.strip()) - Adicione na lista de palavras, as palavras sem o espaço (sem \n)

        # Armazena na variavel a palavra sem o espaço (sem \n)
        v_palavra_sem_espaco = v_palavra.strip()
        # Armazena nas variaveis o tamanho das palavras definidas no dicionário de tamanho com base no seu nivel
        tamanho_min, tamanho_max = dict_tamanho_palavras[v_configuracao_dificuldade]
        # Se o tamanho da palavra for maior que o minimo e menor que o maximo, adicione na lista de palavras
        if tamanho_min <= len(v_palavra_sem_espaco) <= tamanho_max:
            lista_palavras.append(v_palavra_sem_espaco)
# print(lista_palavras)

# Armazena na variavel a quantidade total de palavras que existe na lista, menos 1 por que iniciamos com o indice 0
v_indice_maximo = len(lista_palavras) - 1
# Escolhe aleatoriamente um indice dê uma range que inicia no "a" = 0 e termina no "b" = quantidade máxima
v_indice_aleatorio = random.randint(a=0, b=v_indice_maximo)
# Armazena na variavel o nome da palavra cujo o indice foi escolhido aleatoriamente do arquivo words
v_palavra_selecionada = lista_palavras[v_indice_aleatorio]
# print(v_indice_aleatorio)
print(v_palavra_selecionada)

# Armazena na variavel a quantidade de tentativas que o usuario terá, sendo:
# Nivel de dificuldade igual a 1, o utilizador terá (2 x Tamanho da palavra escolhida aleatoriamente) + 2
# Nível de dificuldade igual a 2, o utilizador terá 2 x Tamnho da palavra escolhida aleatoriamente
# Nível de dificuldade igual a 3, o utilizador téra (2 x Tamanho da palavra escolhida aleatoriamente) - 2
v_total_tentativas = 2 * len(v_palavra_selecionada)
if v_configuracao_dificuldade == "1":
    v_total_tentativas += 2
elif v_configuracao_dificuldade == "3":
    v_total_tentativas -= 2

print(f"A quantidade de tentativas para adivinha a palavra será de {v_total_tentativas}")
