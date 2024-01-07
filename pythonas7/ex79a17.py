'''
pg onde o usuário possa digitar várias valores numéricos e cadastre-os em uma lista. caso o número já exista lá d
entro, ele não será adicionado. no fina, serão exibidos todos os valores únicos digitados, em ordem cerscente.
terminar sim ou não
'''
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? S/N '))
    if r in 'Nn':
        break
print('=-='*30)
# números.sort(reverse=True)
números.sort()
print(f'você digitou os valores {números}')