'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
# def leiaInt(msg):
#     while True:
#         try:
#             n = int(input(msg))
#         except (ValueError, TypeError):
#             print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
#             continue
#         except (KeyboardInterrupt):
#             print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
#             return 'vazio'
#         else:
#             return n
#
#
# num = leiaInt('Digite um valor: ')
# print(f'O valor digitado foi {num}')

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 'vazio'
        else:
            return n
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 'vazio'
        else:
            return n

n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um real: ')

print(f'O valor inteiro digitado foi {n1} e o real é {n2}')