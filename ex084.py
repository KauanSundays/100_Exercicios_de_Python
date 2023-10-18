lista = list()
listb = list()
counter = 0

# Atribuição dos dados nas listas:
while True:
    lista.append(str(input("Nome: \n")))
    lista.append(float(input("Peso (em kg): \n")))

    listb.append(lista[:])
    lista.clear()
    counter += 1

    pergunta = str(input("Continuar? [Sim/Não] \n")).upper()
    if pergunta[0] == "N":
        break

# a) Quantas pessoas foram cadastradas:
print(f"a) {counter} pessoas foram cadastradas.")

# Breve tratamento dos dados contidos nas listas:

pesos = list()  # Lista onde estarão apenas os pesos

for i in listb:
    pesos.append(i[1])

pesos = sorted(pesos)  # Lista onde extrairei o maior e o menor valor.

menor = pesos[0]
maior = pesos[-1]

# b) Pessoas mais pesadas:
mais_pesados = list()
menos_pesados = list()

for k in listb:  # Para cada lista dentro de listb:
    if k[1] == maior:  # Se o peso for igual ao maior
        mais_pesados.append(k[0])  # Adicione seu nome à lista
    if k[1] == menor:  # Se o peso for igual ao menor
        menos_pesados.append(k[0])  # Adicione seu nome à lista

# b) Uma listagem com as pessoas mais pesadas:
print(f" b) O maior peso foi de {maior}kg. Peso de {mais_pesados}")

# c) Uma listagem com as pessoas mais leves:
print(f" c) O menor peso foi de {menor}kg. Peso de {menos_pesados}")

'''
Este programa lê nome e peso de várias pessoas e os armazena em uma lista. Em seguida, ele calcula e exibe:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.
'''
