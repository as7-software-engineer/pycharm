from random import shuffle
n1 = str(input("1st aluno "))
n2 = str(input("2nd aluno "))
n3 = str(input("3rd aluno "))
n4 = str(input("4° aluno "))
lista= [n1, n2, n3, n4]
#embaralhar = shuffle, NOTE QUE EU USEI APENAS  O SHUFFLE, LOGO POSSO USAR NA LINHA 1, APENAs SHUFFLE

shuffle(lista)
print(" a ordem da apresentação será ")
print(lista)

