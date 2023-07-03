import random  #sempre importar o random
n1 = str(input('Nome da primeira pessoa: '))
n2 = str(input('Nome da segunda pessoa: '))
n3 = str(input('Nome da terceira pessoa: '))
n4 = str(input('Nome da quarta pessoa: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem embaralhada será: ')
print(lista)