lista = []
pares = []
impares = []

while True:
    lista.append(int(input("Digite um número: \n")))
    cont = str(input("Quer continuar? \n")).strip().upper()
    if cont[0] == "S":
        print("Continuando.")
    elif cont[0] == "N":
        print("Programa finalizado.")
        break
    else:
        print("Digite uma resposta válida.")

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Lista de números digitados: {lista}.")
print(f"Lista de números pares: {pares}.")
print(f"Lista de números ímpares: {impares}.")

'''
Este código em Python permite ao usuário digitar uma lista de números. Em seguida, ele separa os números em duas listas extras, uma contendo os valores pares e a outra contendo os valores ímpares. Por fim, o programa exibe o conteúdo das três listas geradas: a lista original, a lista de números pares e a lista de números ímpares.
'''
