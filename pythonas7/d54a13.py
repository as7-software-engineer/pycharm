# crie um pg que leia o ano de nascimento de sete pessoas. no final mostre quantos pessoas ainda não atinjiram a maior idade e quantas ja são maiores.
# 21 anos
from datetime import date
aa = date.today().year
tdmaior = 0
tdmenor = 0
for p in range (1,8+1,1):
    adn = int(input(" Ano de nascimento da {}° pessoa?  ".format(p)))

    idade = aa - adn
    print('Essa pesssoa tem {} anos '.format(idade))
    if idade >= 21:
        tdmaior += 1
        # print('Esssa pessoa é maior')
    else:
        tdmenor += 1
        # print('Essa pessoa é menor')
print("Ao todo tivemos {} pesssoas maiores de idade".format(tdmaior))
print("Ao todo tivemos {} pesssoas menores de idade".format(tdmenor))