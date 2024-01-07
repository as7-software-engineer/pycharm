'''pg onde digitamos 7 valores numéricos
e cadatre-os em uma lista única que mantenha separados os valores pares e ímpares no final, mostre os valores
pares e ímpares em ordem cescente.
'''
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
# print(f'Todos os valores: {núm}')
print('=-='*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]} ')
print(f'Os valores ímpares digitados foram: {núm[1]} ')