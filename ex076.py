listagem = (
    "pão", 1,
    "leite", 3.50,
    "frango", 10.90
)

print("=" * 40)
print("{:^40}".format("LISTAGEM DE PREÇOS"))
print("=" * 40)

for i in range(0, len(listagem), 2):
    print("{:<30} R$ {:7.2f}".format(listagem[i], listagem[i + 1]))
