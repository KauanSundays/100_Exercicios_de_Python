lista = [[], []]

for num in range(1, 8):
    numero = int(input((f"Digite um número ({num}/7): \n")))
    if numero % 2 == 0:
        lista[0].append(numero)  # números pares
    else:
        lista[1].append(numero)  # números ímpares

# Números pares em ordem crescente:
print(f"Números pares em ordem crescente: {sorted(lista[0])}")

# Números ímpares em ordem crescente:
print(f"Números ímpares em ordem crescente: {sorted(lista[1])}")

'''
Este programa permite ao usuário digitar sete valores numéricos e os armazena em uma lista única, separando os valores pares e ímpares. Em seguida, ele exibe os valores pares e ímpares em ordem crescente.
'''
