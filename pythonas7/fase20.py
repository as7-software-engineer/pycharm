'''função estão vinculada a uma rotina
ex de funções que eu já utilizava: print() len() input() int()
float()
=====================================================================
posso dar o exemplo de mostralinha(), vou tranfromar isso em uma rotina personalizada, ou melhor. em uma função def
= def = definição de função.
===============================================================
==================================
sitema de alunos
============================
============================
Cadastro de funcionários
============================
============================
erro do sistema
============================
rotina deve ser otimizada.

def mostraLinha():
    print('=====================================================')

mostraLinha()
sitema de alunos
mostraLinha
mostraLinha
Cadastro de funcionários
mostraLinha
erro do sistema
mostraLinha
'''
# #sem função
# print('='*30)
# print('  CURSO EM VIDEO    ')
# print('='*30)
# print('='*30)
# print('  AUGUSTO   ')
# print('='*30)

# def lin(): #com função
#     print('-'*30) # precisamos ter duas linhas vazias, estético python
#

# lin()
# print('  CURSO EM VIDEO    ')
# lin()
# lin()
# print('  AUGUSTO   ')
# lin()
'''============================================================'''
# #otimizando
# print('='*30)
# print('  CURSO EM VIDEO    ')
# print('='*30)
# print('='*30)
# print('  AUGUSTO   ')
# print('='*30)
# # para


# def mensagem(msg):
#     print('======================')
#     print(msg)
#     print'========================')
# '''mensagem('sistema de alunos')'''

# def título(txt):
#     print('-'*30)
#     print(txt)
#     print('-' * 30)
#
#
# título('   curso em vídeo  ')
# título(' python é muiot bom!  ')
# título(' oi  ')# em breve vou aprender a mudular e jogar as funçõies em outro lugar.
# #======================================================================================

#
# def soma(a, b): #passei parâmetros
#     print(f'A = {a} B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
# soma(3,9,5)# tem 3 valores. então não atende a função que pede dois valores
#
#
# #pg principal
# # soma(4,5)
# # soma(8,9)
# # soma(2,1)
# # soma(4) é um erro, pois só tem um parâmetro.
# soma(b=4, a=5)
'''============================================================================='''
'''vamos aprender o conceito de empacotar parâmetros'''
'''
def contador(*num): * siginifica desempacotar, o cara vai passar vários parâmetros, e vc vai pegar todos e jogar dentro de um.

contador(5,7,3,1,4)#vc passou 5 numbers
contador(8,4,7) vc passou 3 numbers
'''
# def contador(*núm):
#     print(núm)
#
#
# contador(2,1,7)
# contador(8,0)
# contador(4,4,7,6,2)
# (2, 1, 7)
# (8, 0)
# (4, 4, 7, 6, 2)

# def contador(*núm):
#     for v in núm:
#         print(v ,end=' ')
#
#
# contador(2,1,7)
# contador(8,0)
# contador(4,4,7,6,2)
'''==========================================================='''
# def contador(*núm): #tuplas. #tuplas. #tuplas.
#     tam = len(núm)
#     print(f'Recebi os valores {núm} e são ao todo {tam} números')
#
#
# contador(2,1,7)
# contador(8,0)
# contador(4,4,7,6,2)
'''==========================================================='''
'''========================listas=========listas==================
vantagem é mutável. 
valores = [7,2,5,0,4]
valores 7   2   5   0   4
indice  0   1   2    3   4       

dobra(valores) vai dobrar os valores.

def dobra(lst):
     pos = 0
     while pos < len(lst):
          lst[pos]*=2
          pos +=1
'''
# def dobra (lst):
#         pos = 0
#         while pos<len(lst):
#             lst[pos] *=2
#             pos +=1
# valores = [6,3,9,1,0,2]
# dobra(valores)
# print(valores)

'''==========================================================='''
'''                        desempacotar       '''
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)











