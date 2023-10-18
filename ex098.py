from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}.")

    if inicio < fim:
        counter = inicio
        while counter <= fim:
            print(f"{counter} ", end="")
            sleep(0.2)
            counter += passo
        print("Fim")
    else:
        counter = inicio
        while counter >= fim:
            print(f"{counter} ", end="")
            sleep(0.2)
            counter -= passo
        print("Fim!")

inicio = int(input("Início: \n"))
fim = int(input("Fim: \n"))
passo = int(input("Passo: \n"))

contador(1, 10, 1)
contador(10, 0, 2)
contador(inicio, fim, passo)
# O código define uma função chamada contador() que realiza contagens de acordo com os parâmetros fornecidos (início, fim e passo).
