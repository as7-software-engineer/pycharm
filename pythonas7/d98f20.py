'''pg que tenha uma função chamada contador (), que receba três parâmetros: início, fim e passo e realize a contagem.
 seu programa tem que realizar três contagens através da função criada:
 a ) de 1 até 10, de 1 em 1
 b) de 10 até 0, de 2 em 2
 c) uma contagem personalizada.
'''
from time import sleep
def contador(i, f, p):
    if p < 0:
        p*=-1
    if p == 0:
        p = 1
    print('=-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i
        while cont<=f:
            sleep(0.3)
            print(f'{cont} ', end="") #flush=True caso não contasse certo.
            cont += p
        print('fim')
    else:
        cont = i
        while cont >= f:
            sleep(0.3)
            print(f'{cont} ', end="") #flush=True caso não contasse certo.
            cont -= p
        print('fim')
    print('=-=' * 20)

#pg main
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)