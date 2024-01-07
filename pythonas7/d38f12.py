# escreva pg q leia dois n int e os compare mostre na tela o primeiro valor é maior o segundo valor é maior-não existe valor maior os dois são iguais
# \033[0;33;44m     #testo, estilo e fundo 3 códigos
# style                         text                 fundo
# 0 none s/estilo              30 white                40
# 1 bold negrito               31 red                  41
# 4 underline sublinhado       32 green                42
# 7 negative                   33 yellow               43
# letra vai pra fundo e        34 blue                 44
# vice-versa                   35 purple               45
#                              36 light blue           46
#                              37 grey                 47
n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite o segundo valor: "))
cores = {"limpa":"\033[m","azul":"\033[34m","amarelo":"\033[33m","pretoebranco":"\033[7:30m","verde":"\033[32m","vermelho":"\033[31m","negritoac":"\033[1;35m"}

if n1>n2:
    print("O primeiro valor é o {}maior{}. ".format(cores["verde"],cores["limpa"]))
elif n2>n1:
    print("O segundo valor é o {}maior{}. ".format(cores["vermelho"],cores["limpa"]))
else:
    print(" Não existe valor maior os dois sao {}iguais{}. ".format(cores["negritoac"],cores["limpa"]))
