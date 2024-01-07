'''pg uqe leia nome e média de um aluno, guardando também a situação em um dicionário. no final
mostre o conteúdoda estrutura na tela.'''
aluno = dict()
aluno['nome'] = str(input(('Nome: ')))
aluno['média'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situaçãu'] = 'Recuperaação'
else:
    aluno['situação'] = 'Reprovado'
# print(aluno)
print('=-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')