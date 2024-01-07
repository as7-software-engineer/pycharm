'''pg tenha uma função fatorial() que receba dois parâmteros: o que indique o número a calcular e o outro chamado show.
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''
def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}',end='')
            if c > 1:
                 print(f' x ',end='')
            else:
                print(f' = ',end='')
        f *= c
    return f

# pg main
# print(fatorial(5))
help(fatorial)