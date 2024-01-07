# pg que jogue jokenpô comigo.
from random import randint
itens=("pedra", "papel","tesoura")
computador = randint(0,2)
# print(" o computador escolheu {} ".format(computador)) retorna 0 1 ou2
# print(" o computador escolheu {} ".format(itens[computador]))
print('''suas opções:
[0] pedra
[1] papel
[2] tesoura
''')
jogador = int(input(" qual é a sua jogada? "))
print("-="*11)
print("computador jogou {}".format(itens[computador]))
print("jogador jogou {}".format(itens[jogador]))
print("-="*11)

if computador == 0:
   if  jogador == 0:
       print("empate")
   elif jogador == 1:
       print("you wins")
   elif jogador == 2:
       print("pc wins")
   else:
       print("jogada inválida")
elif computador == 1:
    if jogador == 0:
        print("pc wins")
    elif jogador == 1:
        print("empate")
    elif jogador == 2:
        print("you wins")
    else:
         print("jogada inválida")

elif computador == 2:
    if jogador == 0:
        print("you wins")
    elif jogador == 1:
        print("pc wins")
    elif jogador == 2:
        print("empate")

    else:
         print("jogada inválida")

