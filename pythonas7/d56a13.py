# pg que leia o nome, idade e sexo de 4 pessoas. no final do pg mostre
# a media de idade do grupo
# qual é o nome do homem mais mais velho:
# quantas mulheres tem menos de 20 anos.
somaidade = 0
mediaidade = 0
ndhmv = 0
midh = 0
mcmd20a=0

for p in range(1,5):
    print("====={}° pessoa =======".format(p))
    ndp = str(input('Nome: ')).strip()
    idp = int(input('idade: '))
    sdp = str(input('sexo [M/F]: ')).strip()
    somaidade += idp
    if p == 1 and sdp in 'mM':
        midh = idp
        ndhmv = ndp
    if sdp in 'mM' and idp > midh:
        midh = idp   # maior idade do homem
        ndhmv = ndp                           #nome do homem mais velho
    if sdp in 'fF' and idp < 20:
        mcmd20a+=1
mediaidade = somaidade / p
print(' A média de idade do grupo é de {} anos. '.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}. '.format(midh, ndhmv))
print('ao total são {} mulheres com menos de 20 anos. '.format(mcmd20a))

