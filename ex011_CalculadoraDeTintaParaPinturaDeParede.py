larg = float(input('Largura de parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de  {}m2'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {} de tinta'.format(tinta))
