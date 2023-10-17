from math import hypot
co = float(input('Cunprimento do cateto oposto: '))
ca = float(input('Cunprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))