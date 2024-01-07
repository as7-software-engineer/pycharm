'''escreva um pg que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci:
    ex:0-1-1-2-3-5-8
       t1 t2 t3     t1 t2 t3...'''
print('-'*30)
print('Sequência de fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-'*30)
print(' {} -> {}'.format(t1,t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1

'''=====================================================
print(' {} -> {} ->'.format(t1,t2), end='')
t3 = t1 + t2
pt = 0
print(' {} '.format(t3), end='')
while c <= n:
    pt = t3 + t2
    t3 = pt
    t2 = t3- 1
    print('-> {} '.format(pt) if c < n else '...', end='')
    c += 1
==================================='''

