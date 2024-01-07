'''pg cria uma matriz 3x3 e prencha com valores lidos pelo teclado.
no final mostre a matriz na tela com a formatação correta.
012 012
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1}, {c+1}]: '))
print('=-=' * 30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^10}]',end="")
    print()

