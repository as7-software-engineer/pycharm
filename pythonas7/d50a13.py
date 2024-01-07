# pg que leia six numbers inteiros e mostre apenas a soma daqueles que forem pares, impar desconsidera.
sdp=0
for c in range (1,6+1,1):
    n = int(input(" digite o {}° número: ".format(c)))
    if n %  2 == 0:
         sdp = sdp + n
print(" a soma de todos pares informados foi de: {}. ".format(sdp))