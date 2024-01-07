'''crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem
da colocação. depois mostre:
a apenas os 5 primeiros colocados.
b os últimos 4 colocados
c uma lista  lista com os times em ordem alfabética
d em que posicão na tabela está i time da chapecoense.
'''
times = ('Corintinhas', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('=-='*40)
print(F'LISTA DE TIMES {times}')
print('=-='*40)
print(f'Os 5 primeiros são {times[0:5]}') #vai mostrar os 5 primeiros times

# print(f'Os 5 primeiros são {times[16:20]}') #vai mostrar os 4 últimos times
print(f'Os 5 primeiros são {times[-4:]}') #vai mostrar os 4 últimos times        obs profesora /raquel.capitalize() vai mostar tudp minúsculo menos a última letra.
print(f' Times em ordem alfabética: {sorted(times)}') # sorted = ordenados, classfificados em ordem.
print(f'O time {times[7]} está na posição {times.index('Chapecoense')+1}')



