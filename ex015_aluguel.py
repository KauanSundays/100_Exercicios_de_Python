dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos KM você andou com o carro? '))
vDias = dias * 60
vKm = km * 0.15
valor = vDias + vKm
print('Você deve pagar: {} reais.'.format(valor))
