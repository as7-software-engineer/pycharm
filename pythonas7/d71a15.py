'''
pg que simule caixa, no início pergunta ao usuário qual seráo valor a ser sacado(número inteiro) e o programa vai informar.
quantas cédulas de cada valor serão entregues.
considere que o caixa possui cédulas de 50, 20. 10 e 1.
'''
print('=' * 30)
print('{:^30}'.format('Banco as7'))
print('=' * 30)
valor = int(input('Que valor você quer sacar?: R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd # vou tirar as notas de 50 possiveis do caixa
        totcéd += 1 # vou acumular todas as notas que foram possiveis de tirar de 50 do valor total.
    else:
        if totcéd > 0:
            print(f'total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('obrigado, tenha um ótimo dia')
