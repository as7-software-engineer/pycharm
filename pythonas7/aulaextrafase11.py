# cores no terminal
# ansi escape sequence
# always que eu quiser representar uma cor, \033[m
#      style   back
# \033[            m   codigo de estilo, texto e de fundo
#           text
# \033[0;33;44m     #testo, estilo e fundo 3 códigos
# style                         text                 fundo
# 0 none s/estilo              30 white                40
# 1 bold negrito               31 red                  41
# 4 underline sublinhado       32 grend                42
# 7 negative                   33 yellow               43
# letra vai pra fundo e        34 blue                 44
# vice-versa                   35 purple               45
#                              36 light blue           46
#                              37 grey                 47
# \033[0;30;41m
# print("\033[4;30;44molá, mundo!\033[m")
# a = 3
# b = 5
# print(" Os valores são \033[32m{} \033[me \033[31m{}. ".format(a,b))

# nome = " augusto "
# print(" fico feiliz em conhecê-lo, {}{}{}!!!!!!! ".format("\033[36m", nome.lower(),"\033[m"))
nome = "augusto"
cores = {"limpa":"\033[m","azul":"\033[34m","amarelo":"\033[33m","pretoebranco":"\033[7:30m"}
print(" fico feiliz em conhecê-lo, {}{}{}!!!!!!! ".format(cores["amarelo"], nome, cores["limpa"]))

