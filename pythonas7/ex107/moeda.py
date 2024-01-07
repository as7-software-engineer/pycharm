'''crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
faça também  um programa que importe esse módulo e use algumas dessas funções.'''


def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res

def diminuir(preço, texa):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res

