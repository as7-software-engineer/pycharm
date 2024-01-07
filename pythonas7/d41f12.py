# a org de natçao precisa de um pg que leia o ano de nascimento de um atleta e mostre a sua categoria de acordo com sua idade:
# ate 9 anos mirim ,ate 14 infantil ,ate 19 anos junior, até 20 anos sênio ,acima master,
from datetime import date
aa = date.today().year
adn = int(input(" Ano de nascimento: "))
idade = aa - adn
print("O atleta tem {} anos ".format(idade))
if idade <= 9:
    print(" Classe: MIRIM ")
elif idade <=14:
    print(" Classe: INFANTIL ")
elif idade <= 19:
    print(" Classe: JUNIOR ")
elif idade <= 25:
    print(" Classe: SÊNIOR ")
else:
    print(" Classe MASTER ")

