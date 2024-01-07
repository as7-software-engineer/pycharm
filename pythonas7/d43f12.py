# pg que ler peso e altura de depois calcula seu imc e mostre seu statsu, tabela < 18.5 abixo do peso
# 18.5 a 25 peso ideal  25 a 30 sobre peso  30 a 40 obesidade  >40 obesidade mórbida
peso = float(input( "qual é o seu peso? (kg) "))
altura = float(input(" qual é a sua altura? (m) "))
imc = peso/(altura**2)
cores = {"limpa":"\033[m","azul":"\033[34m","amarelo":"\033[33m","pretoebranco":"\033[7:30m","verde":"\033[32m","vermelho":"\033[31m","negritoac":"\033[1;35m"}
print(" o imc dessa pessoa é de {:.2f} ".format(imc))
if imc < 18.5:
     print(" você está ABAIXO DO PESO normal")
# elif imc >= 18.5 and imc < 25:
#        ou
elif 18.5 <= imc < 25:
    print(" PARABÉNS, você está na faixa de PESO NORMAL")
elif  25 <= imc <30:
    print(" você está em {}SOBREPESO{}".format(cores["vermelho"],cores["limpa"]))
elif 30 <= imc <40:
    print(" você está em OBSIDADE")
elif 40 <=imc:
    print(" você está em SOBREPESO")

