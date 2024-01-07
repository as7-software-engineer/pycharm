'''listas= variáveis compostas
lenche ('hamburguer', 'suco', 'pizza', 'pudim')
lanche 0 1 2 3
print(lanche[2]) vai mostar a pizza.
lanche[3]= novo
  impossível em tuplas imutáveis.
 obs tuplas usamos ()

     listas usamos []
 lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
 lanche[3]= novo agora dá certo

            ===ADCI0NAR ELEMENTOS================
agora vamos adcionar um novo lanche no final da lista

pois vamos usar  a tag lanche.append('cookie')
para adcionar um lanche. em uma posição a gosto.
lanche.insert(0,'kikão) na posição inicial inserimos o kikão
['kikão','hamburguer', 'suco', 'pizza', 'pudim']

=========DELETAR ELEMENTOS======
comando del para deletar (método)

 lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
del lanche[3] aqui exclui o pudim
lanche.pop(3) indicamos o índice
lanche.pop() aqui excluimos o ultimo elemento da lista.

if 'pizza' in lanche:
     lanche.remove('pizzza') aqui, pra não ocorrer erro no programa, por pizza não existir no vetor
inserimos a estrutura if para burlar o errro. evitando-o.

lanche.remove('pizza") remove o elemento.

 =================criar listas através de range===
 valores = list(range(4,11)) de 4 até 10 +1
 valores 4 5 6 7 8 9 10
         0 1 2 3 4 5 6
     colocar os elementos em ordem.
valores = [8,2,5,4,9,3,0]
valores.sort()
valores 0 2 3 4 5 8 9
        0 1 2 3 4 5 6
            = = = = =  ===ordem reversa.
valores.sort(reverse=True)

=======comprimento da lista===
valores = [8,2,5,4,9,3,0]
len(valores) vai mostrar o número 7 de elementos

'''
# num = [2,5,9,1]
# num[2] = 3 # a lista é mutável
# num.append(7) # insere na ultima posição.
# # num[4] = "augustoso"
# num.sort() #organiza em ordem crescente
# num.insert(2,0) # insere e afasta os demais uma posição para direita.
# num.insert(2,2) #insere na posição 2 o número dois
# num.remove(2) # ele procura do inicio da lista a primeira o correncia qe eu procuro eleiminar.
# if 4 in num:
#     num.remove(4)  # ele procura do inicio da lista a primeira o correncia qe eu procuro eleiminar.
# else:
#     print(' não achei o número 4')
# num.pop(2) #vai pagar o elemento adicionado
# # num.sort(reverse=True) aqui temos a lista ordenada de modo inverso
# print(num) aqui temos a lista ordenada de modo inverso
# print(f'essa lista tem {len(num)} elementos') quantos valores temos
#
# '''criar listas assim '''
# # valores = list() ou valores = []
# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
# # print(valores)
# for v in valores:
#     print(f'{v}...',end='') # aqui mostramos  os núemros 5 9 4
# for c,v in enumerate(valores):
#     print(f' Na posição {c+1} encontri o valor {v}!.') # aqui mostramos  os núemros 5 9 4 e suas devidas posições
# print('Chguei ao final da lista')
# valores = list()
valores = []
# for cont in range(0,5):
#     valores.append(int(input('digite um valor: ')))
# for c, v in enumerate(valores):
#     print(f' na pos {c} encontrei o valor {v}!')

''''============================================================='''
# a = [2,3,4,7]
# b = a
# print(a)     # exemplo 1
# print(b)
''''============================================================='''
# a = [2,3,4,7]
# b = a
# b[2] = 8
# print(a)     # exemplo 2 faço uma ligação de listas, quando eu atualizo uma lista, a outra recebe o valor.
# print(b)
# ''''============================================================='''

# a = [2,3,4,7]
# b = a[:]
# b[2] = 8
# print(a)     # exemplo 3 faço uma ligação de listas, quando eu atualizo uma lista, a outra não recebe o valor.
# print(b)
# ''''============================================================='''

