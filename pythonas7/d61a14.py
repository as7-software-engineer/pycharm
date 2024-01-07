'''
refaça desafio 51 lendo o primeiro termo e a razão de pa, mostrando os 10 primeiros termos da progressão
usando a estrutura while
'''
print('gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
r = int(input('Qual a razão: '))
termo = pt
cont = 1
while cont <= 10:
    print('{}'.format(termo), end='')
    if cont < 10:
        print(" -> ", end='')
    else:
        print(' acabou! ')
    # print(" -> " if cont < 10 else ' acabou ', end='')
    termo += r
    cont += 1