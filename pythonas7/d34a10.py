# pg que recebe salário de um funcionário e mostra p salarios >1250 +10%
# <1250 calcular +15%
print(" REAJUSTE SALARIAL \n > R$1.250,00 = +10% \n < R$1.250,00 = +15%")
dss = float(input(" digite seu salário: "))
sr = 1250
a10 = dss*0.10
a15 = dss*0.15
ssa10 = a10+dss
ssa15 = a15+dss

if dss > sr:
    print(" seu salário teve um aumento de 10% (R${:.2f}) \n Logo seu novo salário é R${:.2f} ".format(a10,ssa10))
else:
    print(" seu salário teve um aumento de 15% (R${:.2f}) \n Logo seu novo salário é R${:.2f} ".format(a15, ssa15))