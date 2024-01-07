# faça um pg que leia um n de 0 a 9999  e mostre na tela cada um dos dígitos separados.
# ex digite um n 1834
# unidade:4
# desena:3
# centena: 8
# milhar: 1

# usando string
# n = str (int(input("digite um número de 0 a 9999: ")))
# print(" unidade:{} ".format(n[3]))
# print(" dezena:{} ".format(n[2]))
# print(" centena:{} ".format(n[1]))
# print(" milhar:{} ".format(n[0]))

n = int(input("digite um número de 0 a 9999: "))
u  = n//1%10
d = n//10%10
c = n//100%10
m = n//1000%10

print(" unidade:{} ".format(u))
print(" dezena:{} ".format(d))
print(" centena:{} ".format(c))
print(" milhar:{} ".format(m))