# '''funções parte 2 vamos falaer sobre:
# interative help = tem a ver com documentações
# docstring = documentação do nosso programa, o nosso programa pode ser documentado.
# argumentos opcionais = funções com argumentos citados
# escopo de variáveis = em que momento nasce e em que momento  morre. em que momentos e posiçoes elas são visíveis.
# é importante para o uso de bibliotecas
# retorno de resultados = pois na aula anterior as funções não retornavam resultados.
# ====================================================================================================
# interativa helps =
# help() = função/ método interna usamos isso no CONSOLE PYTHON
#
# print(input.__doc__)
# ou help(input)
# ==================================================
# docstring = destino da documentação.
# def contador(i,fim,p):
#      """faz um contagem e mostra na tela.
#      :param i:início da contagem
#      :param f:fim da contagem
#      :param p:passo da contagem
#      :return:sem retorno
#      """
#     c=i
#     while <= f:
#         print(f'(c)', end='..')
#         c+=p
#     print('fim!')
#
# contador(2,10,2) existe uma cópia dos valores.
# ou help(contador)
# # '''
# # def contador(i,f,p)
#     """
#     #
#     # :param i:
#     # :param f:
#     # :param p:
#     # :return:
#     """
# ==============================================================
# '''parâmetros opcionais
# def somar(a=0,b=0,c=o):
#     s = a + b + c
#     print(f'A soma vale (s)')
#
#
# somar(3,2,5)
# somar(8,4)
# somar()
# somar(f'A soma vale {s}')
#
# ==================================================================
# escopo de variáveis = em que momento nasce e em que momento  morre. em que momentos e posiçoes elas são visíveis.
# def teste():
#     x = 8
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')
# #pg main
# n = 2
# print(f'No programa principal, n vale {n}')
# teste()
# print(f'no pg main, x vale {x}') #aqui não funciona, pois o x foi uma variável local interna.
# ================================================
# def teste(b):
#     a = 8
#     b +=4
#     c =2
#     print(f'A dentro vale {a}')  8           #b e c escopo local=======
#     print(f'B dentro vale {b}')
#     print(f'C dentri vale {c}')
#
# a = 5                    # escopo global=====
# teste(a)
# print(f'A fora vale {a}') 5
# print(f'B fora vale {b}')xxxxxx
# print(f'C fora vale {c}')  xxxxxxxx'''
# def funcao():
#     n1 = 4
#     print(f'N1 dentro vale {n1} ')
# n1 = 2
# funcao()
# print(f"N1 fora vale {n1}")
# ==================================================
# def teste(b):
#     global a         #escopo local b = 9
#     a = 8                        #  c = 2
#     b += 4
#     c = 2
#     print(f'A dentro vale{a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
# a = 5
# teste(a)
# print(f'A fora vale {a}')             # a = 8
# ====================================================
# # =====retornando valores
#      '''  return'''
# def somar(a=0,b=0,c=0):
#     s=a+b+c
#     print(f'A soma vale {s} ')
#
# somar( 3,2,5)            #
# somar(2,2)
# somar(6)
# A soma vale 10
# A soma vale 4
# A soma vale 6
# '''================================'''
# def somar(a=0,b=0,c=0):
#     s=a+b+c
#     print(f'A soma vale {s} ')
#     return s
# # resp = somar(3,2,5)
# # #ou
# # print(somar(3,2,5))
# #ou
# r1 = somar(3,2,5)
# r2 = somar(1,7)
# r3 = somar(4)
# print(f'Meus cálculos deram {r1}, {r2} e {r3}')
#==============fatorial de um número
# def fatorial(num = 1):
#     f = 1
#     print(f'O fatorial de {num} = ',end='')
#     for c in range(num, 0, -1):
#         f *= c
#         if c > 1:
#             print(f'{c} x ',end='')
#         else:
#             print(f'{c}', end='')
#     return f
# n = int(input('Digite um número: ')) #O fatorial de 10 = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3628800.
# print(f' = {fatorial(n)}.')

# def fatorial(num = 1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
# print(f' o numero é par? {par(num)}')
#ou
if par(num):
    print('É par!')
else:
    print('Não é par!')
