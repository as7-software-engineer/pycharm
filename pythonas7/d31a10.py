# pg que pergunte distancia
# em km de viajem
# # calcule valor do preço da passagem cobrando 0.50 por km de viajem ate 200km
# e 0.45
print(" Vc vai pagar 50 centavos a cada km percorrido até 200km. \n acima de 200, vc vai pagar 45 centavos a cada km. ")
d = float(input(" Qual a distãncia percorrida: "))
# if d>=0 and d<=200:
#     print("vc percorreu {}km, por tanto o valor a ser pago será R$ {:.2f} ".format(d,d*0.5))
# else:
#     print("vc percorreu {}km, por tanto o valor a ser pago será R$ {:.2f} ".format(d,d*0.45))
p = d*0.5 if d <=200 else d*0.45
print(" vc precisa pagar R$ {:.2f} reais. com base nos {} kilmetros percorridos. ".format(p,d))