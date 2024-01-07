'''
pg que leia 5 valores numéricos e guarde-os em uma lista.
no final, mostre qual foi o maior e o menos valor digitado e as suas repectivas posições na lista.
'''
listanum = list()
mai = 0
men = 0
for c in range(0,5,1):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        # mai = c
        # men = c
        mai = men  = listanum[c]
    else:
        if listanum[c] > mai: #and listanum[c] != 0:
            mai = listanum[c]
        if listanum[c] < men: #and listanum[c] != 0:
            men = listanum[c]
print('=-='*30)
print(f'Você digitou os valores {listanum}')
print(f' O maior valor foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f"{i}... ", end='')
print()
print(f' O menor valor foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f"{i}... ", end='')