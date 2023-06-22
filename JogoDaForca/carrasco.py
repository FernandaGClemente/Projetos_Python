from utilitario import exiba_menu_dificuldade, escolha_palavra_aleatoria, obter_total_tentativas
import re


v_configuracao_dificuldade = exiba_menu_dificuldade()
v_palavra_aleatoria = escolha_palavra_aleatoria(v_configuracao_dificuldade=v_configuracao_dificuldade)
# v_obter_tentativas_totais = obter_total_tentativas(v_palavra_selecionada=v_palavra_aleatoria,
# v_configuracao_dificuldade=v_configuracao_dificuldade) v_avaliacao_tentativas = v_obter_tentativas_totais
v_avaliacao_tentativas = v_tentativas_totais = obter_total_tentativas(v_palavra_selecionada=v_palavra_aleatoria,
                                                                            v_configuracao_dificuldade=v_configuracao_dificuldade)
print(f"A quantidade de tentativas para adivinha a palavra será de {v_tentativas_totais}")
estado_atual = ["_" for letras in v_palavra_aleatoria]
lista_letras_adivinhadas = []

while "_" in estado_atual and v_avaliacao_tentativas:
    print(f"\n\n### Tentativa número {v_tentativas_totais-v_avaliacao_tentativas+1} de "
          f"{v_tentativas_totais} ###")
    for v_caracter in estado_atual:
        print(v_caracter, end=" ")

    v_letras_adivinhadas = ""
    while not v_letras_adivinhadas:
        # Aramazena na variavel a letra digitada pelo usuario, guardada em minuscula
        v_letras_adivinhadas = input("\nTente uma letra: ").lower()
        # letras adivinhadas não pode ser vazia e só pode ter apenas uma letra e tem que estar entre a-z minusculo OU
        # Se o tamanho das letras adivinhadas diferir de 1 e não estiver entre a-z minusculo
        if len(v_letras_adivinhadas) != 1 and not re.match("[a-z]", v_letras_adivinhadas):
            print("Entrada inválida. Tente novamente, entrando apenas 1 letra.")
            v_letras_adivinhadas = ""

    # Se a letra digitada não tiver na lista de letras adivinhadas, então adicione-a
    if v_letras_adivinhadas not in lista_letras_adivinhadas:
        lista_letras_adivinhadas.append(v_letras_adivinhadas)
        # Se a letra adivinhada estiver contida na palavra escolhida aleatoriamente
        lista_posicao = []
        v_indice_posicao = 0
        for letras in v_palavra_aleatoria:
            if letras == v_letras_adivinhadas:
                lista_posicao.append(v_indice_posicao)
            v_indice_posicao += 1

            for v_indice_posicao in lista_posicao:
                estado_atual[v_indice_posicao] = v_letras_adivinhadas
        else:
            # Diminua uma tentativa da quantidade de tentativas
            v_avaliacao_tentativas -= 1
    else:
        # Se a letra digitada estiver na lista, informe:
        print(F"{v_letras_adivinhadas} já foi tentado anteriormente.")
