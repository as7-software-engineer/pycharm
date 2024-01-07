'''pg que tenha uma função chamada ficha(), que receba dois parâmetros opicionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamenete.
'''
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols')



# pg main
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)