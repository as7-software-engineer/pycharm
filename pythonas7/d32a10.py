# pg que receba ano qualquer e diga se é um ano bissexto
from datetime import date
a = int(input(" que ano quer analisar? Coloque 0 para analisar o ano atual"))
if a == 0:
    a = date.today().year
if a % 4 ==0 and a % 100 != 0 or a % 400 == 0:
    print("o ano é bissexto")
else:
    print("o ano não é bissexto.")