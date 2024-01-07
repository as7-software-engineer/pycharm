'''tenha função notas() que pode receber várias notas de alunose vai retornar um dicionário com as seguintes informações
quantidade de notas; a maior nota; A menor nota; A média da turma;A situação (opcional)
Adicione também as docstrings da função.
'''
def notas(*n, sit=True):
    """
    -> função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param n: valor opicional, indicando se deve ou não adicionar a situação
    :param sit: valor opcional, indicando se deve ou não adcionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    # print(r)
    return r

#pg main
resp = notas(7, 7, 7,7)
# print(resp)
help(notas)




