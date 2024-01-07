''' dados = list()     adicioando valores no final na lista vazia.
dados.append('pedro)
dados = ['pedro']
dados.append(25)
dados = ['pedro', 25]
print(dados[0]) pedro
print(dados[1]) 25
==========================lista dentro das listas============
pessoas = list()
pessoas.append(dados[:]) vou adicionar toda uma estruta na poiscção 0 de pessoas []
 0 1   0 1    0 1
  0     1      2
  pessoas = [["pedro",25],['maria',19],['joão',32]]
print(pessoas[0][0]) pedro
print (pessoas[1][1]) 19
print(pessoas[1]) ['maria',19] mostar tudo da lista indice 1
'''
# teste = list()
# teste.append('gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste)
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste)    #nesse primero momento gerou [[maria,22],[maria ,22]]
# # print(teste)
# print(galera)

# teste = list()
# teste.append('gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])    #nesse momento gerou [[gustavo,40],[maria ,22]]
# # print(teste)
# print(galera)
#===============================================================
# galera = [['joão', 19], ['Ana', 33], ['joaquim', 13], ['maria', 45]]
# print(galera[0][0]) #joão
# print(galera[0]) #['joão', 19]
# print(galera) #[['joão', 19], ['Ana', 33], ['joaquim', 13], ['maria', 45]]
# print(galera[2][1]) #13

# galera = [['joão', 19], ['Ana', 33], ['joaquim', 13], ['maria', 45]]
# for p in galera:
#     # print(p) # pessoa e idade ['joao',19]...
#     # print(p[0])  # pessoa  joao...
#     # print(p[1])  # idade 19...
#     print(f'{p[0]} tem {p[1]} anos de idade.')
#     =============================================================
#                      vamos pegar uma lista e adcionar uma lista temporária dentro dela
# galera = list()
# dado = list()
# for c in range(0,3,1):
#     dado.append(str(input(' Nome: ')))
#     dado.append(int(input(' Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
# print(galera) #[['as', 5], ['sd', 6], ['ag', 7]]
#             mostar pessoas que tem mais de 21 anos.
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3,1):
    dado.append(str(input(' Nome: ')))
    dado.append(int(input(' Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        totmai +=1
        print(f'{p[0]} é maior de idade.')
    else:
        totmen +=1
        print(f'{p[0]} é menor de idade.')


