valor = float(input(" quantos reais você tem? \n vamos converter este valor, \n a fim de saber quantos dólares você pode obter  "))
d = 3.27 # 1 dólar = 3.27 reais
vc = valor/d
print(' com {:.2f} reais, você pode adquirir {:.2f} dólares. '.format(valor,vc))