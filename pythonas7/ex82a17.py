'''crie um pg que vai ler vários nmrs e colocar em uma lista.
depois disso, crie duas listas extras que vão conter apenas os valores pares e o valores ímpares digitados,
respectivamente.
ao final mostre o conteúdo das três listas geradas.
sim ou não
'''
num = list()
pares = list()
ímpares  = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print('=-=' * 30)
print(f'A lista completa é {num}')
print(f'a lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')