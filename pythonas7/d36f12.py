# escreva um pg para aprovar um emprestimo bancário para a compra de uma casa. o pg vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestação mensal, sabando que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# # my
# vdc = float(input(" valor da casa: R$ "))
# sdp = float(input(" digite seu salário: R$ "))
# app = int(input(" quantos anos você deseja ficar pagando as parcelas: "))
# mdpap = app*12
# vappcp = vdc/mdpap
# vprpa = sdp*0.3
# cores = {"limpa":"\033[m","azul":"\033[34m","amarelo":"\033[33m","pretoebranco":"\033[7:30m","verde":"\033[32m","vermelho":"\033[31m","negritoac":"\033[1;35m"}
# print(" analisando suas informações...")
# print(" De acordo com seu perfil, seu plano de pagamento é \n       Pagar       \n valor de cada parcela: R$ {:.2f} \n Mêses a pagar: {} meses. ".format(vappcp,mdpap))
# if vappcp < vprpa:
#     print(" empréstimo \n status: {}APROVADADO{} ".format(cores["verde"],cores["limpa"]))
# else:
#     print(" empréstimo \n status: {}NEGADO{} ".format(cores["vermelho"],cores["limpa"]))

casa = float(input(" valor da casa: R$"))
salario = float(input(" salario do comprador: R$"))
anos = int(input(" quantos anos de financiamento?"))
prestacao = casa / (anos*12)
minimo = salario*(30/100)
print("para pagar uma casa de R${:.2f} em {} anos ".format(casa, anos), end="")
print("a prestação será de R${:.2f}".format(prestacao))
if prestacao <= minimo:
    print("empréstimo pode ser \033[32mCONCEDIDO\033[m!")
else:
    print("empréstimo \033[31mNEGADO\033[m!")