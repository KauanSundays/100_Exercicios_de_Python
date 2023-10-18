prim = int(input("Primeiro termo: \n"))
raz = int(input("Razão da PA: \n"))

counter = 1
termo = prim
tam = 10  # Quantidade de termos a serem mostrados inicialmente
more_terms = True

while more_terms:
    while counter <= tam:
        print(termo, end=" -> ")
        termo += raz
        counter += 1

    user = int(input("Mais termos (digite 0 para encerrar): \n"))

    if user == 0:
        more_terms = False
    else:
        tam = user

print("Fim.")
