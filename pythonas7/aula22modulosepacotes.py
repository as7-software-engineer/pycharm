'''Modularização
surgiu no início da década de 60; sistemas ficando cada vez maiores; foco: dividir um grande programa;
foco: aumentar a legibilidade; foco: facilitar a manuntenção.

def fatorial(n):
    f=1                                   uteis.py
    for c in range(n,0,-1):          def fatorial(n):
        f*=c                          ...........
    return f                          ...........


def dobro(n):                            ..............
    return  n * 2                          ..........


def triplo(n):                              .............
    return n * 3                           ............



num = int(input("Digite um valor"))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}
===========================================================
import uteis #o ideal
# from uteis import fatorial, dobro # o que vale é a ultima a ser importada.


num = int(input("Digite um valor: "))
fat = uteis.fatorial(num)
print(f"O fatorial de {num} é {fat}. ")
print(f'O dobro de {num} é {uteis.dobro(num)}')
# num = int(input("Digite um valor: "))
# fat = fatorial(num)
# print(f"O fatorial de {num} é {fat}. ")
# print(f'O dobro de {num} é {dobro(num)}')
===========================================vantagens da modularizaçãoxxxxxxx////////
organização do código; facilidade na manuntenção; ocultação de código detalhado; reutilização em outros projetos;
=======================pacotes?================xxxxxxxxxxxxxxxxxxxxx////////////////
várias modularizações. eu irei separar por assuntos dentro de um pacote com o nome que escolher, no caso do exemplo
anterior: pacotes uteis
assuntos; numeros; strings, cores, datas e etc
============================ posso também fazer importações.
pacotes uteis.
from uteis; from uteis import datas;from uteis import cores;
=================como faço para criar os pacotes.
crio uma pasta
        uteis
            __init__.py
            CORES
                __init__.py
            datas
                __init__.py
            números
                __init__.py
            strings
                __init__.py





















'''