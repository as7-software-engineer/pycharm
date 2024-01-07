'''
pg que leia nome e preço de vários produtos. o pg dever´perguntar se o usuário vai continuar. No final, mostre:
A. qual é o total gasto na compra.
B. quantos produtos custam mais de 1000.
c. nome do produto mais barato.
'''
total = totmil = pmb = 0
pc = 1
pasm =' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$:'))
    total += preço
    if preço > 1000:
        totmil += 1
        '''======================================================'''

    # if pc == 1:
    #     pmb = preço
    #     pasm = produto
    # else:
    #     if preço < pmb:
    #         pmb = preço
    #         pasm = produto
    if pc == 1 or preço < pmb:
            pmb = preço
            pasm = produto
            '''======================================================'''

    pc += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f"{' fim do programa ':=^40}")
# print('{:-^40}'.format('fim do pg'))
print(f'O total da compra foi {total:10.2f}')
print(f'temos {totmil} produtos custando mais de 1000 reias.')
print(f"O produto mais barato é {pasm} que custou {pmb}")
