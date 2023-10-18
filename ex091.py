from random import randint

players = dict()

print("Valores sorteados:\n")
for i in range(4):
    jogada = randint(1, 6)
    players[f"jogador {i + 1}"] = jogada
    print(f"O jogador {i + 1} tirou {jogada} pontos no dado.")

print("\nRanking dos jogadores:")
players_list = sorted(
    list(zip(players.values(), players.keys())), reverse=True)

for i, player in enumerate(players_list):
    print(
        f"{i + 1}º lugar: {players_list[i][1]} com {players_list[i][0]} pontos")

'''
Este programa permite que quatro jogadores joguem um dado e guarde os resultados em um dicionário. Em seguida, ele determina o vencedor com base no número mais alto e exibe o ranking dos jogadores com base nos pontos obtidos.
'''
