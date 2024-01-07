'''pg que leia nome e peso de várias pessoas, guardando tudo em uma lista. no final, mostre:
a) quantas pessoas foram cadastradas.
b)uma listagem com as pessoas mais pesadas.
c) uma listagem com as pessoas mais leves.
'''
# eu não posso fazer isso pois, senão sou ligar duas listas e receber dados duplicados. temp = princ = []
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input("Peso: ")))
    if len(princ) == 0:
       mai = men = temp[1] # 1 é o peso das pessoas.
    else:
        if temp [1] > mai:
            mai = temp[1]
        if temp [1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear() #se su não usar essse comando, a lista vai ter repetição.
    resp = str(input("Quer continuar? [S/N] "))
    if resp in 'Nn':
        break
print('=-='*30)
# print(f'Os dados foram {princ}')
print(f"Ao todo, você cadastrou {len(princ)} pessoas.")
print(f'O maior peso foi de {mai} kg. Peso de ', end="")
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} ',end='')
print()
print(f'O menor peso foi de {men} kg. Peso de ', end="")
for p in princ:
    if p[1] == men:
        print(f'{p[0]} ',end='')