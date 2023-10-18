sex = str(input("Digite M ou F: \n")).strip().upper()[0]
while sex not in "MmFf":
    sex = str(input("Digite apenas M ou F: \n")).strip().upper()[0]
print("Sexo {} registrado com sucesso.".format(sex))
# Lê o sexo de uma pessoa, aceitando apenas "M" ou "F", e pede a digitação novamente em caso de valor incorreto.
