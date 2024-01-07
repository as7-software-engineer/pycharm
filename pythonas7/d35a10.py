# pg que leia 3 valores e verifique se forma um triangulo
print(" digite 3 valores, e eu verei se é possível formar um triângulo! \n regra: a<+b+c")
la = float(input(" digite o lado A: "))
lb = float(input(" digite o lado B: "))
lc = float(input(" digite o lado C: "))
if la < lb+lc and lb <la+lc and lc < la+lb:
    print(" de acordo com os valores, é possivel sim! ")
    if la == lb  == lc:
        print(" o triângulo é equilátero. ")
    elif la != lb != lc and la != lc:
        print(" o triângulo é escaleno. ")
    else: #= lc != lb or lb == lc != la:
        print(" o triângulo é isósceles. ")
else:
    print(" não é possivel formar um triângulo")