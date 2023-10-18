person_dict = dict()
general_info, names, names_quantity, ages, women, above_mean = list(), list(), list(), list(), list(), list()

while True:
    # Recebe nome:
    person_dict['name'] = input("Nome: \n")

    # Recebe sexo:
    sex = input("Sexo [M/F]: \n")
    sex = sex[0].upper()
    person_dict['sex'] = sex

    # Recebe idade:
    person_dict['age'] = float(input("Idade: \n"))
    
    # Insere os dicionários na lista:
    general_info.append(person_dict.copy())

    # Continuar ou sair?
    leave = input("Continuar? [S/N] \n")
    leave = leave.upper()
    if leave[0] == "N":
        break

for dictionary in general_info:
    # a) Quantas pessoas foram cadastradas:
    names_quantity.append(dictionary.get("name"))

    # b) A média de idade do grupo:
    ages.append(dictionary.get("age"))
    age_mean = sum(ages) / len(ages)

    # c) Uma lista com todas as mulheres:
    for key, value in dictionary.items():
        if value == "F":
            women.append(dictionary.get("name"))

    # d) Uma lista com todas as pessoas com idade acima da média:
    if dictionary.get("age") > age_mean:
        above_mean.append(dictionary.get("name"))

print(f"Pessoas cadastradas: {len(names_quantity)}")
print(f"Idade média do grupo: {age_mean:.1f} anos.")
print(f"Mulheres do grupo: {women}")
print(f"Pessoas com idade acima da média: {above_mean}")
