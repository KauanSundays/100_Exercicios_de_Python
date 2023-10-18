prim = int(input("Primeiro termo: \n"))
raz = int(input("Razão da PA: \n"))

dec = (prim + (10 - 1) * raz)  # Fórmula do enésimo termo (PA).

counter = prim
while counter <= dec:
    print("{}".format(counter))
    counter += raz
# Lê o primeiro termo e a razão de uma PA e mostra os 10 primeiros termos da progressão utilizando a estrutura while.
