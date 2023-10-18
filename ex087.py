lista = list()
listb = list()

for i in range(0, 3):  # Para cada linha
    for j in range(0, 3):  # Para cada coluna em cada linha
        listb.append(int(input(f"Digite um valor para [{i}, {j}]: \n")))

    lista.append(listb[:])  # Copie a linha para listb
    listb.clear()

for l in lista:
    print(l)

# a) Soma de todos os valores pares digitados
soma_pares = 0
for i in range(3):
    for j in range(3):
        if lista[i][j] % 2 == 0:
            soma_pares += lista[i][j]

# b) Soma dos valores da terceira coluna
soma_terceira_coluna = 0
for i in range(3):
    soma_terceira_coluna += lista[i][2]

# c) Maior valor da segunda linha
maior_segunda_linha = max(lista[1])

# Exibindo os resultados
print(f"a) Soma dos valores pares: {soma_pares}.")
print(f"b) Soma da terceira coluna: {soma_terceira_coluna}.")
print(f"c) Maior valor da segunda linha: {maior_segunda_linha}.")

'''
Este programa cria uma matriz 3x3, preenche-a com valores lidos pelo teclado e depois apresenta:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
'''
