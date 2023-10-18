import pyautogui as pg
import time
import pyperclip

pg.PAUSE = 0.25

#pega o retorno da posicao atual de x e y do mouse e passa o valor da tupla para as duas variaveis

time.sleep(2)
x, y = pg.position()
print ("Posicao atual do mouse:")
print (str(x)+" , "+str(y))


    