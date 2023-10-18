flag = False
counter = adder = mean = highest = lowest = 0

while flag == False:
    n = int(input("Digite um número inteiro: \n"))

    #  Média:
    adder += n
    counter += 1
    mean = (adder / counter)

    #  Maior/Menor:
    if n > highest:
        highest = n
    if lowest == 0:
        lowest = n
    if n < lowest:
        lowest = n

    #  Continuação:
    cont = str(input("Quer continuar? [SIM / NÃO] \n")).strip().upper()
    if cont == "NÃO":
        flag = True

print("Média: {:.1f}".format(mean))
print("Maior: {} | Menor: {}".format(highest, lowest))
# Lê vários números inteiros, calcula a média, e encontra o maior e o menor valor, permitindo que o usuário decida continuar ou não.
