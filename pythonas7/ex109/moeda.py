'''modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando
se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

def aumentar(preço, taxa = 0, Formato=False):
    """

    :param preço:
    :param taxa:
    :param Formato:
    :return:
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

