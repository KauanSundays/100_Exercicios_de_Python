preco = float(input('Digite o valor do produto a ter desconto: '))
desc = preco / 20
print('O valor do produto com desconto é: {:.2f}, estará economizando {:.2f} reais'.format(preco-desc, desc))