counter = 1
tupla = []

# Ler 4 valores pelo teclado:
while counter < 5:
    n = int(input(f"Digite um número ({counter}/4): \n"))
    tupla.append(n)
    counter += 1

# guardá-los em uma tupla:
tupla = tuple(tupla)
print(f"Tupla: {tupla}")

# a) quantas vezes apareceu o valor 9
nove = tupla.count(9)
print(f"a) O valor 9 aparece {nove} vezes.")

# b) em que posição foi digitado o primeiro valor 3:

if 3 in tupla:
    print(f"b) O primeiro 3 está na posição: {tupla.index(3) + 1}.")
else:
    print("b) O número 3 não está presente.")
# c) quais foram os números pares:

pares = [num for num in tupla if num % 2 == 0]
print(f"c) Números pares: {pares}")
# Lê 4 valores, guarda em uma tupla e mostra quantas vezes o valor 9 apareceu, em que posição foi digitado o primeiro valor 3 e quais são os números pares.
