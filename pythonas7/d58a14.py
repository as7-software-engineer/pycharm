'''melhore o jogo do desafio 028 onde o computador vai (pensar) wm um número
entre 0 e 10. só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpoites foram necessários para vencer.'''
from random import randint
computador = randint(0,10)
print('sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input(" Qual é o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('''mais...tente outro:''')
    elif jogador > computador:
        print('''menos...tente outro:''')
print('Acertou com {} palpites. '.format(palpites))
