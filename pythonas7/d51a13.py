# desenvolva um pg que leia o primeiro termo e a razão de uma pa. no final mostre os 10 primeiros termos dessa progressão.
pt = int(input(" Primeiro termo: "))
r = int(input(" Razão: "))
et = pt + (10-1)* r
for c in range (pt,et+r,r):
    print(' {} '.format(c), end=' -> ')
print('Acabou')