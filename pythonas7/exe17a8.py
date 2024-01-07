from math import hypot
# import math
co = float (input("comprimento do cateto oposto:"))
ca = float (input("comprimento do cateto adjascente:"))
# h = (co**2+ca**2)**(1/2)
# print(" a hipotenusa tem o valor de {:.2f} ".format(h))
h= hypot(co, ca)
# h= math.hypot(co, ca)
print(" a hipotenusa tem o valor de {:.2f} ".format(h))

