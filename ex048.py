s = 0  
for num in range(1, 501):
    if num % 2 != 0:
        if num % 3 == 0:
            s += num
print("A soma dos múltiplos é: {}.".format(s))
# Calcula a soma dos números ímpares e múltiplos de 3 de 1 a 500.
