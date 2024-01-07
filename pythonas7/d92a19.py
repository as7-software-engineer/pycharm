'''crie um pg que leia nome, ano de nascimento e carteira de trbalho e cadastre-os (com idade) em um dicionário sepor acaso
a ctps for diferente de zero, o dicionário receberá também o ano de contração e o salário. calcule e acrescente, além da
idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tenho): '))
if dados['ctps'] !=0:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')