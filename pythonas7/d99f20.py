'''faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros:
seu pg tem que analisar todos os valores e dizer qual é o maior.'''
from time import sleep
def maior(*núm): # utilizando o asterístico vamos poder trabalhar com inúmeros parãmetros, usando estrutura de repetição
    cont = maior = 0
    print('\nAnalisandoos valores passados...')
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

# pg principal
maior(2,9,4,5,7,1)
maior(4, 7, 0)
maior(1,2)
maior(6)
maior()