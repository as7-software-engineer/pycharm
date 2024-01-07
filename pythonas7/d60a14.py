'''pg que leia um número qualquer
e mostre o seu fatorial.
ex: 5! = 5x4x3x2x1=120'''
'''==========================================================='''
# from math import factorial
# n = int(input('Digite um número para calcular seu factorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n,f))
'''============================================================'''

n = int(input('Digite um número para calcular seu factorial: '))
c = n
f = 1
print('calculando {}!'.format(n), end=' = ')
while c > 0:
    print('{}'.format(c), end="")

    f = f * c
    c -= 1
print(f)
# print('{} '.format(c))
