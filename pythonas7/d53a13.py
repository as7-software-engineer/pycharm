# pg que leia uma frase qq e diga se ela é um polindromo, desconsiderando os espaços.
# ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona.
# frase = str(input('Digite um a frase: ')).strip().upper()
# # print(len(frase))
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# # print(' vc digitou a frase {}'.format(palavras))
# # print(' vc digitou a frase {}'.format(junto))
# for letra in range(len(junto) - 1, -1, -1):
#     inverso+=junto[letra]
# print(' o inverso de {} é {}'.format(junto, inverso))
# if inverso == junto:
#     print('temos um palíndromo!')
# else:
#     print('não é palíndromo')
frase = str(input('Digite um a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso== junto:
    print('temos um palíndromo!')
else:
    print('não é palíndromo')
