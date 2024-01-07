'''
existem 3 tipos de variáveis compostas. tuplas , listas e as tuplas.
temos elementos diferentes identificados por índices.
as string são variáveis compostas.
  lenche
  o san , 1 suco, 2 pizza 3 pudim
  print(lanche[2]) vai mostrar pizza)
  print(lache [0:2]) vai mostrar o sanduiche até o suco (0 e 1)
  print(lanche [1:]) vai mostrar o primeiros indic 1 até o final.
  print(lanche[-1]) vai mostar o ultimo elemento, no caso o pudim
length(comprimento)
  len(lanche) vai mostrar 4.

  lanche
  0 1 2 3       pao suco pizza pudim                c = 0
  for c in lanche:                                  c = 1
   print(c)                                         c = 2
                                                    c = 3
 usamos o for para vc (tuplas)                      depois sai do looping
AS TUPLAS SÃO IMUTÁVEIS.
TEMOS QUE PARAR O PG PARA ALTERAR A TUPLA.
posso começar uma vc de três maneiras (tupla) [lista] {dicionário}
'''
# lanche = 'hamburguer'
# lanche = 'suco'
# print(lanche)  vai mostrar suco,perdeu lanche

# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# print(lanche)                   mostra tudo

# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# print(lanche[1]) mostra o suco
'''==================================='''
# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# print(lanche[-1],end=' ')
# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# print(lanche[-2], end=' ')
'''==================================='''
# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# #tuplas are imutáveis
# # lanche[1] = 'refri'
# print(lanche)                  # mostra tudo

# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')
'''==================================='''
# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# print(len(lanche))                                     mostra a quantidade dos elementos.
# print('Comi pra caramba!')

# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# for comida in range(0,len(lanche)):           mostra 0 1 2 3
#     print(comida)
'''===================================''''''==================================='''
# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# for comida in range(0,len(lanche)):     #mostra os laches hamb suco pizza pudim
#     print(f'eu vou comer {lanche[comida]}')

# lanche = ('hamburguer', 'suco', 'pizza', 'pudim') #mostra os laches hamb suco pizza pudim
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')
'''===================================''''''==================================='''
                       # podemos mostrar a posição de cada ação.
'''===================================''''''==================================='''
# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# for comida in range(0,len(lanche)):     #mostra os laches hamb suco pizza pudim  # podemos mostrar a posição de cada ação.
#     print(f'eu vou comer {lanche[comida]} na posição {comida}')

# lanche = ('hamburguer', 'suco', 'pizza', 'pudim') #mostra os laches hamb suco pizza pudim
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')
# print('Comi pra caramba!')
'''===================================''''''==================================='''
# lanche = ('hamburguer', 'suco', 'pizza', 'pudim') #mostra os laches hamb suco pizza pudim
# # sorted = ordenado, coloca em ordem.
# print(sorted(lanche))
# print(lanche)
'''===================================''''''==================================='''
# a = (2,5,4)
# b = (5, 8, 1, 2)
# c = a +b   # concatenou as tuplas.   mostrou (2,5,4, 5 ,8,1,2)
# print(len(c))
# print(c)
# print(c.count(5)) # quantas vezes ta aparecendo o n 5.
# print(c.index(8)) # em que posição aprece o 8./
# print(c.index(2,1)) #comecei a analisar na posição 1 então vai mostrar o 2 na posião 6
'''===================================''''''==================================='''
pessoa = ("gustavo", 39, 'm',99.88)
del(pessoa) # apaga da memória todas as informações da variável. não apago os índices sozinhos, mas a tupla inteira sim.
print(pessoa)






