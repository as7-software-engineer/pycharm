# import uteis #o ideal
# from uteis import fatorial, dobro # o que vale é a ultima a ser importada.
from uteis import numeros


num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}. ")
print(f'O dobro de {num} é {numeros.dobro(num)}')
# num = int(input("Digite um valor: "))
# fat = fatorial(num)
# print(f"O fatorial de {num} é {fat}. ")
# print(f'O dobro de {num} é {dobro(num)}')