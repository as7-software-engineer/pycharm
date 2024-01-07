# for c in range(1,6):  #para c no range de 1 até 5, posição 6 nao faz parte da contagem
#     print('oi')
# print("fim")
# =========================
# for c in range(0,6):  #para c no range de 0 até 5, posição 6 nao faz parte da contagem
#     print(c)
# print("fim")
# =========================
# for c in range(6,0,-1):  #para c no range de 6 até 1, posição 0 nao faz parte da contagem
#     print(c)
# print("fim")
# =========================
# for c in range(6,-1,-1):  #para c no range de 6 até 1, posição 0 nao faz parte da contagem
#     print(c)
# print("fim")
# =========================
# n = int(input('digite um número'))
# for c in range(0,n+1):
#     print(c)
# print("fim")
# =========================
# i = int(input('início: '))
# f = int(input('fim: '))
# p = int(input('passo: '))
# for c in range(i, f+1,p):
#     print(c)
# print('fim')
# =========================
s=0
for c in range(0,4):
    n = int(input('digite um valor: '))
    # s = s + n
       # ou
    s += n
    print('o somatório de todos os valores foi {}. '.format(s))