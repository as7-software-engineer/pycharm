''' pg que jogue par ou ímpar com o computador. O jogo é interrompido quando o jogador perder.
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

'''
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ìmpar [P/I] ')).strip().upper()[0]
    print(f'Vc jogou {jogador} e o computador {computador}. total de {total}', end='')
    print('Deu par' if total % 2 == 0 else 'Deu ìmpar' )
    if tipo == 'P':
        if total % 2 == 0:
            print('Vc Venceu!')
            v += 1
        else:
            print(f'Vc perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Vc Venceu!')
            v += 1
        else:
            print(f'Vc perdeu')
            break
    print('Vamos jogar novamente...')
print(f" Game Over! Vc venceu {v} vezes.")