from random import randint
# gerar 5 números e colocar numa tupla:
tupla = ()
for _ in range(5):
    tupla += (randint(0, 100),)

# listagem de números gerados:
print("Valores sorteados: ", end="")
for num in tupla:
    print(f"{num} ", end="")

# menor e maior valores:
menor = min(tupla)
maior = max(tupla)

print(f"\nMenor: {menor}")
print(f"Maior: {maior}")
# Gera 5 números aleatórios, coloca-os em uma tupla e mostra a listagem, o menor e o maior valor da tupla.
