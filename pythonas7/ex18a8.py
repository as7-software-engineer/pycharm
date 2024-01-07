import math
ângulo = float(input("digite o angulo que você deseja: "))
seno = math.sin(math.radians(ângulo))
print("o angulo de {} tem o SENO de {:.2f}".format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print("o angulo de {} tem cosseno de {:.2f}".format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print("o angulo de {} tem tangente de {:.2f}".format(ângulo, tangente))

