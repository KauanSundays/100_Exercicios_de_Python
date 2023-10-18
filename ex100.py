from random import randint
from time import sleep

def sorteia():
    numeros = list()
    for n in range(0, 5):
        numeros.append(randint(0, 99))
    print(f"Sorteando {len(numeros)} valores da lista: ", end="")
    for i in numeros:
        print(f"{i} ", end="")
        sleep(0.5)
    return numeros

def soma_par(lista_numeros):
    pares = list()
    for n in lista_numeros:
        if n % 2 == 0:
            pares.append(n)
    print(f"\nOs valores pares da lista são: ", end="")
    print(f"{pares}", end="")
    print(f"\nE a soma deles é: {sum(pares)}")

soma_par(sorteia())
# O código define duas funções: sorteia() para gerar uma lista de números aleatórios e soma_par() para mostrar os valores pares e a soma deles.
