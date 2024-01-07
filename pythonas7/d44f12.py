# pg q calcula o valor a ser pago recebendo preço normal e condição de pagamento:
# - á vista dinheiro ou cheque 10 % de desconto
# a vista no cartão 5% de desconto
# em até 2 x no cartão preço normal
# 3x ou mais no crtão 20% de juros
cores = {"limpa":"\033[m","azul":"\033[34m","amarelo":"\033[33m","pretoebranco":"\033[7:30m","verde":"\033[32m","vermelho":"\033[31m","negritoac":"\033[1;35m"}
print("{:=^40}".format( "loja  v// "))
p = float(input("preço das compras: R$"))
print(''' FORMAS DE PAGAMENTO
[1] À VISTA dinheiro / cheque
[2] À VISTA CARTÃO 
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO''')
o = int(input(" qual é a opção? "))
if o == 1:
    total = p - (0.1*p)
elif o == 2:
    total = p - (p*0.05)
elif o == 3:
    total = p
    parcela = total/2
    print(" sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif o == 4:
    total = p*1.20
    totaldeparcelas = int(input(" quantas parcelas você tanka pagar?"))
    parcela = total/totaldeparcelas
    print(" sua compra será parcelada em {}x de {} reias com juros." .format(totaldeparcelas,parcela))
else:
    total = p
    print(" {}OPÇÃO INVÁLIDA de pagamento. Tente novamente!{}".format(cores["vermelho"],cores["limpa"]))
print("sua compra de R${:.2f} vai custar R${} no final.".format(p, total))

