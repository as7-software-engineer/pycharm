'''
melhorar desafio 61, perguntando para o usuário se ela quer mostar mais alguns termos . o programa encerra quando ele disse que quer mostar 0 termos.
'''
print('gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
r = int(input('Qual a razão: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você que mostrar a mais?'))
print('pa finalizada com {} termos no total'.format(total))