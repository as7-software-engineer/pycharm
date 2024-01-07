'''pg que leia nome e duas notas de vários alunos e gaurde tudo em uma lista composta. No final, mostre um boletim
 contendo a média de cada um e permita que o usuário possa mostar as notas de cada aluno individualmete.
'''
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2],media])
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
print('=-=' * 30)
print(f'{"no.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]}')
while True:
    print('-' * 35)
    opc = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
