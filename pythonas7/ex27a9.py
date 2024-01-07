# fç um pg que leia , mostre o primeiro e ultimo nome
# ex: anamaria de souza
# primeiro= ana
# ultimo = souza
n = str(input(" digite seu nome completo: ")).title().strip()
ns = n.split()
print(" seu primeiro nome é {} ".format(ns[0]))
print(" ultima palavra de seu nome é {} ".format(ns[len(ns)-1]))