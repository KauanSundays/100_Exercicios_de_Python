# Declarando variáveis
lista = list()
listb = list()

# Preenchendo a matriz 3x3 com valores lidos pelo teclado
for i in range(0, 3):  # Para cada linha
    for j in range(0, 3):  # Para cada coluna em cada linha
        listb.append(int(input(f"Digite um valor para [{i}, {j}]: \n")))

    lista.append(listb[:])  # Copiando a linha para listb
    listb.clear()

# Mostrando a matriz na tela com a formatação correta
for l in lista:
    print(l)
    
'''
Este programa cria uma matriz 3x3 e preenche com valores lidos pelo teclado. Em seguida, exibe a matriz na tela com a formatação correta.
'''
