'''pg onde o usuário posssa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção. sem usar sort()).
no final mosstre a lista ordenada na tela.
'''
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    # if c == 0:
    #     lista.append(n)
    # elif n > lista[len(lista)-1]:
    #     lista.append(n)
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print("=-="*30)
print(f"Os valores digitados em ordem foram {lista}")