# crie um pg que leia o nome de uma pessoa e diga se ela tem "silva" no nome
n = str(input("digite seu nome: ")).strip()
print(" Você tem silva em seu nome: {} ".format("SILVA" in n.upper()))