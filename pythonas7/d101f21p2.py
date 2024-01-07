'''pg que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um
valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
'''



def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade <18 or idade > 65:
        return f'Com {idade} anos, seu voto é OPCIONAL (16-17).'
    else:
        return f'Com {idade} anos seu voto é OBRIGATÓRIO. (18+)'


# pg main
nasc = int(input('Em que ano vc nasceu? '))
print(voto(nasc))