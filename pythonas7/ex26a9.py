# fç um pg que leia uma frase pelo teclado e mostre:
# quantas vezes a letra aparece
# posição que ela aparece pela primera vez.
# posição que ela aparece pela ultimaa vez.

f = str(input(" digite uma frase: ")).upper().strip()
print(" A letra A aparece {} vezes na frase.".format(f.count("A")))
print(" A primeira letra A apareceu na posição {} ".format(f.find("A")+1))
print(" A ultima letra A apareceu na posição {} ".format(f.rfind("A")+1))