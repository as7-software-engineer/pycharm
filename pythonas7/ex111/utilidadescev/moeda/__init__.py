'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.

Tranfira todos as funções utilizados nos dessafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
'''

def aumentar(preço, taxa = 0, Formato=False):
    """
    ->Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento.
    :param Formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preço + (preço * taxa/100)
    return res if format is False else moeda(res)

def diminuir(preço = 0, taxa = 0,Formato = False):
    res = preço - (preço * taxa/100)
    return res if format is False else moeda(res)


def dobro(preço = 0, formato = False):
    res = preço * 2
    return res if not format else moeda(res)


def metade(preço = 0, Formato = False):
    res = preço / 2
    return res if not Formato else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0, taxaa= 10, taxar = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}') #\t tabulação
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)

