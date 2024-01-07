''' crie um pg que leia nome. sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
 os dicionários em uma lista. no final, mostre:
 A quantas pessoas foram cadastrdas
 b a médoa de idadedo grupo
 c uma lista com todos as mulheres
 d uma lista com todas as pessoas com idade acima da média.
'''
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [M/f] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.')
    while True:
        pessoa['idade'] = int(input('Idade: '))
        soma += pessoa['idade']
        # galera = pessoa[:] erro
        galera.append(pessoa.copy())
        if pessoa['idade'] > 0:
            break
        print('digite um número maior que 0.')
    while True:
        resp = (str(input("Quer continuar? [S/N]"))).upper()[0]
        if resp in "SN":
            break
        print("digite apenas sim ou não porra!")
    if resp in 'N':
        break                                                '''LEITURA DE DADOS'''
        '''=============================================================================================================='''
print('=-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média: 5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p ['sexo'] == 'F':
        print(f"{p['nome']}, ", end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
if p in galera:
    if p['idade'] >= média:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')                              '''RESULTADO, ANALISANDO OS DADOS QUE ESTÃO DENTRO DA LISTA E AI SIM, MOSTRANDO O RESULTADO FINAL.'''
'''================================================================================================='''