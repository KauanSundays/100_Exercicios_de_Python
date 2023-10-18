num1 = float(input("Digite um número (1/2): \n"))
num2 = float(input("Digite outro número (2/2): \n"))
menu = (
'''\nMENU PRINCIPAL:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] Sair do programa\n'''
)
maior = 0
menor = 0

print(menu)

user = int(input("Sua escolha (opções de 1 a 5): \n"))
while user != 5:
    if user > 5 or user < 1:  # Verifica se a escolha está dentro das opções
        print("Escolha inválida. Digite um número de 1 a 5.")
        user = int(input("Sua escolha: \n"))
    else:
        if user == 1:  # Soma
            print("Você escolheu soma!")
            print("Resultado da soma: \n{} + {} = {}".format(num1, num2, (num1 + num2)))
            user = int(input("Sua escolha: \n"))
        elif user == 2:  # Multiplicação
            print("Você escolheu multiplicação!")
            print("Resultado da multiplicação: \n{} x {} = {:.0f}".format(num1, num2, (num1 * num2)))
            user = int(input("Sua escolha: \n"))
        elif user == 3:  # Maior ou menor
            if num1 > num2:
                maior = num1
                menor = num2
                print("O maior é {} e o menor é {}.".format(maior, menor))
            elif num2 > num1:
                maior = num2
                menor = num1
                print("O maior é {} e o menor é {}.".format(maior, menor))
            else:
                print("Os dois números são idênticos.")
            user = int(input("Sua escolha: \n"))
        elif user == 4:  # Novos números
            new_num1 = float(input("Novo número 1: \n"))
            new_num2 = float(input("Novo número 2: \n"))
            num1 = new_num1
            num2 = new_num2
            user = int(input("Sua escolha: \n"))
print("Opção 5: Programa encerrado.")
# O programa lê dois números, oferece um menu de opções ao usuário e executa a operação escolhida, permitindo também escolher novos números ou sair do programa.
