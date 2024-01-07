'''
pg que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre:
a) quantas vezes apareceu o valor 9.
b) em que posição foi digitado o primeiro valor 3.
c) quais foram os números pares.
'''
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite o último número: ')))
print(f'Vc digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
       print(f'o primeiro valor 3 digitado,foi na posição {núm.index(3)+1}.')
else:
       print(f'o valor 3 não foi digitado. ')
print('os pares digitados foram os valores: ',end='')
for n in núm:
       if n % 2 == 0 and n != 0:
              print(f' {n} ',end='')