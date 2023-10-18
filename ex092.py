worker_infos = dict()

name = input("Digite um nome: \n")
birthday = input("Data de nascimento: \n")
ctps = int(input("Número da carteira de trabalho (CTPS): \n"))

retirement_age = int()
age = int()

worker_infos["name"] = name
worker_infos["birthday"] = birthday
worker_infos["ctps"] = ctps

if ctps != 0:
    hiring_date = input("Data de contratação: \n")
    salary = int(input("Salário: \nR$ "))

    worker_infos["hiring date"] = hiring_date
    worker_infos["salary"] = salary

# Calcula a idade da pessoa com base no ano de nascimento
birth_year = int(birthday.split("/")[-1])
current_year = 2023  # Ano atual (pode ser alterado)
age = current_year - birth_year

# Calcula o ano de aposentadoria
if "hiring date" in worker_infos:
    hiring_year = int(hiring_date.split("/")[-1])
    years_of_contribution = current_year - hiring_year
    retirement_age = age + (35 - years_of_contribution)
else:
    retirement_age = "N/A"

worker_infos["age"] = age
worker_infos["retirement age"] = retirement_age

print(worker_infos)

'''
Este programa coleta informações sobre uma pessoa, incluindo nome, data de nascimento, número da carteira de trabalho (CTPS), data de contratação e salário (se disponível). Em seguida, ele calcula a idade da pessoa com base no ano de nascimento e, se aplicável, calcula o ano em que a pessoa vai se aposentar com base em 35 anos de contribuição. Por fim, exibe as informações coletadas no dicionário.
'''
