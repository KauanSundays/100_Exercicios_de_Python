s = 0
for i in range(0, 6):
    num = int(input("Digite um número: \n"))
    if num % 2 == 0:
        s += num
print("Somas: {}.".format(s))  
# Mostra a soma dos números pares entre os seis números lidos.
