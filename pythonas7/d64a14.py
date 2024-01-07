'''pg que leia vários n inteiros pelo teclado. o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. no final mostre quantos números foram digitados e a soma entre eles'''
# desconsiderando  o flag.
'''========================================='''
# n = 1
# tdnd = 0
# sdnd = 0
# while n != 999:
#     n = int(input(" digite um número: "))
#     if n!=999:
#         tdnd +=1
#         sdnd += n
# print('''Foram digitados um total de {}.
# A soma de todos eles é {}'''.format(tdnd,sdnd))
'''========================================='''
# n = c = s = 0
# while n != 999:
#     n = int(input('Digite um número [999 para parar]: '))
#     s += n
#     c += 1
# print('Vc digitou {} número e a soma entre eles foi {}.'.format(c-1, s-999))

n = c = s = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Vc digitou {} número e a soma entre eles foi {}.'.format(c-1, s-999))
