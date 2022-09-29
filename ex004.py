a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a)) #mostrará qual é o tipo da variavel
print('É somente espaços?', a.isspace()) #mostra se é somente espaço a msg
print('É um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Está em maisculas?', a.isupper())
print('Esta em minusculas?', a.islower())
print('Está capitalizada?', a.istitle())