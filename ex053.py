frase = str(input("Palíndromo: \n")).upper()
frase = "".join(frase.split(" "))
print("A palavra {} ao contrário é {} e ".format(frase, frase[::-1]), end="")
if frase == frase[::-1]:
    print("é um palíndromo.")
else:
    print("não é um palíndromo.")
# Verifica se a frase fornecida pelo usuário é um palíndromo (lê-se igual de trás para frente, desconsiderando espaços).
