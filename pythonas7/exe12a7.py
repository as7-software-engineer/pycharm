p = float(input('qual é o preço? '))
vd = 0.05*p
nvap = p*0.95
print('você tem 5% de desconto \n valor de referência = {:.2f} reais \n valor descontado = {:.2f} reais \n novo valor a pagar = {} reais '.format(p,vd,nvap))