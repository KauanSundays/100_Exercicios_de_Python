#Este projeto Verifica se o nome digitado tem Silva
nome = str(input('Qual é o seu nome completo')).strip()
print('Seu nome tem Silva {}'.format('silva' in nome.lower()))