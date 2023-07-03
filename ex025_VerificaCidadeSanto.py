#Neste exercicio, estamos verificando se a cidade começa com santo ou não

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')