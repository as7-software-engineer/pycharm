# pg q fç o pc pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escoliho pelo
# if pc:
#     o usuario venceu ou perdeu
from random import randint
from time import sleep
# import random
# n = random.randint(0,5)
n = randint(0,5)
print("_=_"*20)
i = int(input(" tente advinhar o número de 0 a 5 que eu pensei:  "))
print("_=_"*20)
print("processando...")
sleep(3)
if i==n:
       print("você acertou, pois eu pensei em {} e você digitou {}. ".format(n,i))
else:
       print("você nao acertou, pois eu pensei em {} e você disse {}. ".format(n,i))
print("obrigado por jogar.")
