numeros = []

for i in range(5):
    numeros.append(int(input(f"Digite o {i + 1}º número: ")))

maior = max(numeros)
menor = min(numeros)

posicoes_maior = [i for i, num in enumerate(numeros) if num == maior]
posicoes_menor = [i for i, num in enumerate(numeros) if num == menor]

print(f"Você digitou os valores: {numeros}.")
print(f"O maior valor digitado foi {maior} na(s) posição(ões): {posicoes_maior}.")
print(f"O menor valor digitado foi {menor} na(s) posição(ões): {posicoes_menor}.")

# Este código lê 5 números, armazena-os em uma lista e encontra o maior, o menor valor e suas posições.
