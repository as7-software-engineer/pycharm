'''pg que tenha uma função chamada área(), que receba as dimensões de um terreno retangular( largura e comprimento) e
mostre a área do terreno.
'''
def área(l, c):
    a = l*c
    print(f' A área do terreno de comprimento {c} x {l} de largura, é igual a {a:.2f} metros quadrados.')


print(' Controle de terrenos ')
print('-'*20)
l = float(input('LARGURA: (m)'))
c = float(input('COMPRIMENTO: (m)'))
área(l,c)
