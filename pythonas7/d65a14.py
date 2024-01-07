''' pg que leia vrios inteiros pelo teclado. no final da execução. mostre a média entre todos os valores e qual foi o maior e menor valor lido.
o programa deve perguntar ao usu-ario se ele quer conmtinuar ou não a digitar valores'''
# mdvd = maiorvl = menorvl = sdvd = qdvd = 0
# r = "S"
# i = 1
# while r == "S":
#     n = int(input("Digite o {}° número: ".format(i)))
#     sdvd += n
#     qdvd += 1
#     if i == 1:
#         maiorvl = n
#         menorvl = n
#     if n > maiorvl:
#         maiorvl = n
#     if n < menorvl:
#         menorvl = n
#     r = str(input("Quer continuar?[S/N]")).strip().upper()[0]
#     i += 1
# # print(r)
# mdvd = sdvd/qdvd
# print('''A média dos valores digitados foi de {}.
# O maior valor digitado foi {}.
# O menor valor digitado foi {}.'''.format(mdvd,maiorvl,menorvl))

resp = 'S'
soma = quant = média = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? '))
média = soma / quant
print(' vc digitou {} números e a média foi {}.' format(quant, média))
print(" O maior valor foi {} e o menor foi {}". format(maior,menor))


