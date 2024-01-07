#crie um pg que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo".
c = str(input(" em que cidade você nasceu? ")).strip()

print(c[0:5].upper()=="SANTO")
print(len(c))