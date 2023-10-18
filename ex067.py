counter = 1

while True:
    n = int(input("Qual tabuada você quer?: \n"))
    if n < 0:
        break
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")        
print("Programa encerrado.")
# Mostra a tabuada de vários números digitados pelo usuário, encerrando quando um número negativo é inserido.
