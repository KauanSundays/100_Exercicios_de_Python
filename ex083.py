lista = []
exp = str(input("Digite uma expressão: \n"))

for simb in exp:
    if simb == "(":
        lista.append(simb)
    elif simb == ")":
        if len(lista) > 0:
            lista.pop(-1)
        else:
            lista.append(")")
            break

print(f"Lista: {lista}")

if len(lista) == 0:
    print("Válido")
else:
    print("Inválido")

'''
Este código em Python permite ao usuário digitar uma expressão contendo parênteses e verifica se a expressão possui parênteses abertos e fechados na ordem correta. O programa cria uma lista para rastrear os parênteses e, ao final, determina se a expressão é válida ou inválida com base na presença e ordem dos parênteses.
'''

