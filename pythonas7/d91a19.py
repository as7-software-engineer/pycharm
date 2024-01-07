'''pg onde 4 jogadores jogam um dado e tenham resultados aleatórios. guarde essses resultados
em um dicioário. no final,. coloque esse dicionárioem ordem, sabendo que o vencedor tirou o maior número no dado.
'''
# from random import randint
# from time import sleep
# from operator import itemgetter
# jogo = {'jogador1': randint(1,6),
#         'jogador2': randint(1,6),
#         'jogador3': randint(1,6),
#         'jogador4': randint(1,6)}
# ranking = dict()
# print('Valores sorteados: ')
# "para cada chave e valor vou mostrar"
# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(1)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
# # print(ranking)
# c = 1
# for k, v in ranking:
#     print(f'{k} foi o {c}° colocado tirando {v} no dado. ')
#     if k:
#         c+=1
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('Valores sorteados: ')
"para cada chave e valor vou mostrar"
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
print('=-='*30)
print('  == RANKING DOS JOGADORES==')
# print(ranking)
for i, v in enumerate(ranking):
    print(f'   {i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
