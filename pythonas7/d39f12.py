# pg que leia o ano de nascimento e informe de acordo com sua idade:
# se ele ainda vai se alistar no exército
# se é hora de se alistar
# se já passou do tempo do alistamento
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# adn = int(input(" digite o ano de seu nascimento:"))
# at = 2023
# ia = at - adn
# ide = 18
# print(" você tem {} anos. ".format(ia))
# if ia < ide:
#     print(" Você ainda não vai se alistar. \nPois, você só poderá fazer isso em {} ano(s). ". format(ide-ia))
# elif ia == ide:
#     print(" Você deve se alistar! ")
# else:
#     print(" Você já se alistou ou passou da idade requerida. \nVocê já se alistou ou passou do prazo do mesmo, a cerca de {} anos. ".format(ia-ide))

from datetime import date
from time import sleep
atual = date.today().year
nasc = int(input("ano de nascimento: "))
idade = atual - nasc
print("quem nasceu em {} tem {} anos em {}. ".format(nasc,idade,atual))
print("precessando o resto das informações...")
sleep(7)
if idade == 18:
    print(" vc deve se alistar imediatamente! ")
elif idade < 18:
    saldo = 18-idade
    ada = atual + saldo
    print(" ainda faltam {} anos para o alistamento. ".format(saldo))
    print(" o seu alistamento será em {}. ".format(ada))
else:
    saldo = idade - 18
    ada = atual - saldo
    print(" você já deveria ter se alistado há {} anos. ".format(saldo))
    print(" seu alistamento foi em {}. ".format(ada))


