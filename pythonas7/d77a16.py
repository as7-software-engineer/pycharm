'''
pg que tenha uma tupla com várias palavras(não use acentos).
depois disso, vc deve mostrar, para cada palavra, quais são as suas vogais.
'''
words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in words: #para cada palavra na variável palavras faça
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: # para cada letra em uma palavra, verificar uma vogal
        if letra.lower() in 'aeiou': # se letra na lista aeiou fazer:
            print(letra, end=' ')