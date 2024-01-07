''' Variáveis compostas dicionários
                   dados
             'pedro' 24
                0     1

dados = list()                           tuplas ()
dados.append('pedro')                    listas []
dados.append(25)                         dicionários{}
print(dados[0]) pedro
print(dados[1]) 25
===========================================================
                         dados
                         'pedro'   25
                          nome     idade

dados=dict() ou
dados = {'nome':'Pedro','idade':25}                    'nome' identificador do elemento
print(dados['nome']) pedro                             'pedro' valor
print(dados['idade']) 25
=================================================================================
agora para adcionar elementos ?
append não funciona em dicionários.
então....................................
dados['sexo']="M"
                                 dados
                            'Pedro'  25          'M'
                            nome     idade       sexo
=====================================================
agora para remover elementos?
usamos o del.
então...............................................
dados['sexo'] = 'M'
del dados['idade']
   logo             dados
                'pedro'    'M'
                  nome      sexo
===================================================================
                        filme
         'star Wars' 1977  'George Lucas'                   o python chama esses elementos de chaves, keys.
          título

filme = {'titulo':'Star Wars',
         'ano': 1977,
         'diretor':'George Lucas"
}
eu posso acessar a cada momento o item, valor ou chave.

print(filme.values()) vai imprimir os valores de cima (star wars e tals)
método interno representado pelo parênteses.

print(filme.keys()) vai  mostar as chaves(t[itulo, ano, e diretor).

agora se eu quiser pegar tanto o value quantos as keys.
print(filme.items())

posso usar isso nos laços, parecido com o enumerate.
for k,v in filme.items()
   print(f'o (k) é (v)') o título é star wars
                         o ano é 1977
                         o diretor é george lucas
===============================================================

eu posso criar uma lista locadora, e dá um append em uma lista onde em cada elemento tem um dicionário
      'stars' '1977' 'george lucas'    'avangers' '2012' joss whedon'    'matrix' 1999  'wachowski'
      título   ano     diretor         título   ano     diretor           título   ano     diretor
               1                                    2                               3
as listas são identificadas por números, os dionários superam isso.
valores literais, chaves literais.
ptint(locadora[0]['ano']) 1977
print(locadora[2]['título']) matriz
      '''

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# # print(pessoas) #{'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# # print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #O Gustavo tem 22 anos
# # print(pessoas.keys()) #dict_keys(['nome', 'sexo', 'idade'])
# # print(pessoas.values()) #dict_values(['Gustavo', 'M', 22])
# # print(pessoas.items())#dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
# '''========================================================================'''
# # for k in pessoas.values():
#     # print(k) #nome
#              #sexo
#             #idade
#     # print(k) Gustavo
#     #          M
#     #          22
# '''para usar o items preciso usar chave  e o valor'''
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# # no dicionário usamos o items. e not enumerate.

#para excluirmos, temos o comando
# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# del pessoas["sexo"]
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
#     # nome = Gustavo
#     # idade = 22

# '''posso modificar também'''
# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# pessoas['nome'] = 'Leadro'
# pessoas['peso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
#     # nome = Leadro
#     # sexo = M
    # idade = 22
'''======================================================================'''
# brasil = []
# estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'são paulo', 'sigla': 'sp'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(estado1, end='')
# print(estado2) #{'uf': 'Rio de janeiro', 'sigla': 'RJ'}{'uf': 'Rio de janeiro', 'sigla': 'RJ'}
# print(brasil[0]['uf']) #Rio de janeiro
# print(brasil[1]['sigla']) #sp

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    # brasil.append(estado[:]) # não posso fazer fatiamento em dicionário.
    brasil.append(estado.copy())
# print(brasil)
for e in brasil:
    for v in e.values():
        print(v,end=' ')
    print()
    # for k, v in e.items():
    #     print(f'O campo {k} tem valor {v}.')
# [{'uf': 'rio de janeiro', 'sigla': 'rj'}, {'uf': 'são paulo ', 'sigla': 'sp'}, {'uf': 'goias', 'sigla': 'go'}]
# O campo uf tem valor rio de janeiro.
# O campo sigla tem valor rj.
# O campo uf tem valor são paulo .
# O campo sigla tem valor sp.
# O campo uf tem valor goias.
# O campo sigla tem valor go.










