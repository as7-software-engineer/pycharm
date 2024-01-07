#estrura de repretição com teste lógico. (while)
#estrutura de repetição com variavel de controle (for)
'''for c in range(1,10+1,1):
    print(c)
print('Fim')'''
'''c = 10
while c > 0:
    print(c)
    c-=1'''
# =======================
# c=1
# while c <= 10:
#     print(c)
#     c+=1
# print('fIM')
#====================================
# n = 1
# while n != 0:
#     n= int(input('Digite um valor'))
# print('Fim')
#============================================
# r='s'
# while r == 's':
#     n = int(input('Digite um valor: '))
#     r = str(input('quer continuar? [s/n]')).upper()
# print('Fim')
# #=======================================

n = 1
pc = ic =0
while n != 0:
    n= int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            pc+=1
        else:
            ic += 1
print(" você digitou {} números ímpares e {} números pares. ".format(ic,pc))