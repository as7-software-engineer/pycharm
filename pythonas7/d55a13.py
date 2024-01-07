# paça  um pg que leia o peso de cinco pessoas. final . mostre qual foi o maior e o menor peso lidos.
pdmaiorp = 0
pdmenorp = 0
for p in range(1,5+1,1):
    pdp = float(input("Peso da {}° pessoa: ".format(p)))
    if p == 1:
        pdmaiorp = pdp
        pdmenorp = pdp
    else:
        if pdp > pdmaiorp:
            pdmaiorp = pdp
        if pdp < pdmenorp:
            pdmenorp = pdp
print('''O maior peso lido foi de {} kg. 
O menor peso lido foi de {} Kg. '''.format(pdmaiorp,pdmenorp))