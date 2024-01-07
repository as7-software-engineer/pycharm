n1 = (int(input(' digite one number: ')))
n2 = (int(input(' digite outro valor: ')))
s = n1+n2
p = n1*n2
d = n1/n2
di = n1//n2
rdd= n1%n2

print(' a soma entre {} e {} é {}, \n o produto entre {} e {} é {}, \n a divisão entre {} e {} é {:.3f}, \n a divisão inteira é {}, \n o resto da divisão é {} '.format(n1,n2,s,n1,n2,p,n1,n2,d,di,rdd))
