# len = comprimento len(frase)
# frase.count(´0´,0,13) # contar o 0 do inicio ate a posição 13
# curso em vi    d  e  o   p  y  t  h  o  n
#   012345678910   11 12 13  14 15 16 17 18 19 20 21
# frase.find("deo") (11posicaoiniciou)
# "curso" in frase True ou False
# frase.find("android") (-1) nao tem na frASE

#tranformação de string
# frase.replace("python","android") substituiçao de forma secundária
# + funcionalidades
# frase.upper() todaa as letras minusculas tornam-se maiúsculas
# + método transformação ou funçao de string
# frase.lower() retorna tudo que tava em maísculo em minúsculo
# frase.capitalize()  joga tudo para minúsculo, dixando somente a primeira em maísculo
#  frase.title() deixa dos as palavras com inicial em maísculo.
# frase.strip() remove os espaços do inicio e do final de uma sequência ou frase.
# frase.rstrip() remove os espaços a direita
# frase.lstrip() remove os espaços a esquerda

# divisao de strings
# frase.split() gera uma lista com todas as pavras em cadeia de caractere
# curso em video
# 0123  01 0123
#   0    1   2

# junção de string
# "-".join(frase)
# curso-em-video
# 0123456789
# frase = "curso em video"
# print(frase[3:13])
# frase = "curso em video"
# print(frase[:14])
# frase = "curso em video"
# print(frase[3:14])
# frase = "curso em video"
# print(frase[0:14:2]) #sei o o len=comprimento inteiro, uma letra sim e uma letra nao
# print(frase[::2]) #nao sei o inicio nao sei o final da string, mas vou mostrar com um saldo de dois em dois
# print(frase[:14:2]) sei o final da string, mas vou mostrar com um saldo de dois em dois
# print(frase[0::2]) #sei o inicio da string, mas vou mostrar com um saldo de dois em dois
# print("oi")
# print("""kdjnjkdfjgijgfdhgrhhhhrhergh
# rgrgrhgryhra
# ergrgerge
# rtgerger
# gereeg""")
# frase = "curso em video python"
# print(frase.upper().count("O"))
# frase = "curso em video python"
# print(len(frase))
# frase = "curso em video python"
# print(frase.replace("video","augustoso"))
# frase = "curso em video python"
# frase = frase.replace("video", "augustoso")
# print(frase)
# frase = "curso em video python"
# print("curso" in frase)
# frase = "curso em video python"
# print(frase.lower().find("video"))
# frase = "curso em video python"
# dividido = frase.split()
# print(dividido[1][1]) mostra o primeiro elemento da lista[] , mostra a letra[]
# # junto = print(frase.join(frase))