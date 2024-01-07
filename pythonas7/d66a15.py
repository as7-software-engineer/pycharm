'''pg que ler vários números interios. pelo teclado
O programa só vai parar quando o usuário digitar o valor 999. condição de parada.
no fim mostar quantos números foram digitados e qual foi a soma entre eles.
'''
# maneira com gambiarra
# n = soma = 0
# while num != 999:
#     n = int(input('Digite um valor (999 para parar): '))
#     soma += num
# soma-=999
# print(f"A soma dos valores foi {soma}")

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"A soma dos {cont} valores foi {soma}")