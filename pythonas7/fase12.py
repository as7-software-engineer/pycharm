# condições aninhadas, quando colocamos estruturas condicionais uma dentro da outra.
# if
# else
#     if
#     elif
#     else
#         dentro de cada segmento temos um bloco a ser excutado nas estruturas blobo  1 ate bloco...
# n = str(input("qual o seu nome?")).strip().upper()
# if n == "AUGUSTO    ":
#     print(" que nome bonito! ")
# print(" tenha um bom dia {} ".format(n))  condição simples

# condição composta - estrutura condicional aninhada, uma dentro da outra
n = str(input("qual o seu nome?")).strip().upper()
if n == "AUGUSTO":
    print(" \033[36mque nome bonito\033[m! ")
elif n == "PEDRO" or n == "MARIA" or n == "PAULO":
    print("seu nome é bem popular no brasil.")
elif n in "AUGUSTO CESAR FIGUEIRA DOS SANTOS JUNIOR":
    print("belo nome de macho")
else:
    print(" \033[31mseu nome é bem normal\033[m...")
print(" tenha um bom dia {}{}{} ".format("\033[7;30m",n,"\033[m"))