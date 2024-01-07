# pg que leia velocidade de um carro
# se ele ultrapassar 80km/h
# a multa vai custar 7 por cada km a cima do limite
v = float(input( "qual é a velocicade atual do carro? "))
if v>80:
    print("MULTADO! você excedeu o limite permitido que é de 80Km/h")
    multa = (v-80)*7
    print(" você deve pagar uma multa de R${:.2f}! ".format(multa))
print("tenha um bom dia! dirija com segurança!")