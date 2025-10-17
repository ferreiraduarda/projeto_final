# Importa a função randrange() da biblioteca random
# Ela será usada para o computador escolher uma jogada aleatória.
from random import randrange

# Função: exibir_tabuleiro(tabuleiro)
# Mostra o estado atual do jogo em formato visual no console.
# Os números representam casas livres; 'X' e 'O' são jogadas feitas.
def exibir_tabuleiro(tabuleiro):
    print("+-------+-------+-------+")
    for linha in tabuleiro:
        print("|       |       |       |")
        print("|", end="")
        for casa in linha:
            # Centraliza cada elemento (número, X ou O) dentro da célula
            print(f"   {casa:^3}|", end="")
        print("\n|       |       |       |")
        print("+-------+-------+-------+")

# Função: jogada_usuario(tabuleiro)
# Pede ao jogador para escolher uma casa de 1 a 9.
# Verifica se a entrada é válida, dentro do intervalo e se a casa está livre.
# Atualiza o tabuleiro com o símbolo 'O' do jogador.
def jogada_usuario(tabuleiro):
    valido = False
    while not valido:
        movimento = input("Digite o número do campo (1-9): ")

        # Verifica se o valor é um número
        if not movimento.isdigit():
            print("Entrada inválida. Digite um número.")
            continue

        movimento = int(movimento)

        # Verifica se o número está dentro do intervalo de 1 a 9
        if movimento < 1 or movimento > 9:
            print("Movimento fora do intervalo.")
            continue

        # Converte o número da casa em coordenadas da matriz (linha e coluna)
        linha = (movimento - 1) // 3
        coluna = (movimento - 1) % 3

        # Verifica se a casa escolhida está livre
        if tabuleiro[linha][coluna] in ['O', 'X']:
            print("Campo ocupado. Escolha outro.")
            continue

        # Atualiza o tabuleiro com a jogada do usuário
        tabuleiro[linha][coluna] = 'O'
        valido = True

# Função: listar_campos_livres(tabuleiro)
# Retorna uma lista com todas as posições ainda livres no tabuleiro.
# Cada posição é representada como uma tupla (linha, coluna).
def listar_campos_livres(tabuleiro):
    livres = []
    for l in range(3):
        for c in range(3):
            if tabuleiro[l][c] not in ['O', 'X']:
                livres.append((l, c))
    return livres

# Função: verificar_vitoria(tabuleiro, simbolo)
# Analisa o estado do tabuleiro e verifica se o jogador indicado (X ou O)
# venceu o jogo. Retorna True se houver vitória.
def verificar_vitoria(tabuleiro, simbolo):
    # Verifica as 3 linhas
    for linha in tabuleiro:
        if all(casa == simbolo for casa in linha):
            return True

    # Verifica as 3 colunas
    for c in range(3):
        if all(tabuleiro[l][c] == simbolo for l in range(3)):
            return True

    # Verifica as 2 diagonais
    if all(tabuleiro[i][i] == simbolo for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == simbolo for i in range(3)):
        return True

    # Caso contrário, ninguém venceu ainda
    return False

# Função: jogada_computador(tabuleiro)
# O computador faz uma jogada simples e aleatória em uma das casas livres.
# Não utiliza inteligência artificial.
def jogada_computador(tabuleiro):
    livres = listar_campos_livres(tabuleiro)
    if livres:
        linha, coluna = livres[randrange(len(livres))]
        tabuleiro[linha][coluna] = 'X'

#PROGRAMA PRINCIPAL
# Cria o tabuleiro inicial:
# O computador (X) começa jogando no centro, conforme o enunciado.
tabuleiro = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]

# Loop principal do jogo
while True:
    # Mostra o tabuleiro atualizado
    exibir_tabuleiro(tabuleiro)

    # Verifica se o computador venceu
    if verificar_vitoria(tabuleiro, 'X'):
        print("O computador venceu!")
        break

    # Verifica se não há mais jogadas possíveis (empate)
    if not listar_campos_livres(tabuleiro):
        print("Empate!")
        break

    # Solicita e realiza a jogada do usuário
    jogada_usuario(tabuleiro)

    # Verifica se o jogador venceu
    if verificar_vitoria(tabuleiro, 'O'):
        exibir_tabuleiro(tabuleiro)
        print("Você venceu!")
        break

    # Verifica novamente se o tabuleiro ficou cheio (empate)
    if not listar_campos_livres(tabuleiro):
        exibir_tabuleiro(tabuleiro)
        print("Empate!")
        break

    # Joga o computador (movimento aleatório)
    jogada_computador(tabuleiro)