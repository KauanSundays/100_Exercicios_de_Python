prim = int(input("Primeiro termo: \n"))
raz = int(input("Digite a razão da PA: \n"))
dec = prim + (10 - 1) * raz
for c in range(prim, dec, raz):
    print("{}".format(c), end=",")
print("\nFim.") 
# Mostra os 10 primeiros termos de uma Progressão Aritmética com o primeiro termo e a razão fornecidos pelo usuário.
