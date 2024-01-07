# crie um pg que calcule a soma entre todos os números ímpares que são múltiplos de três a que se encontram no intervalo
# de 1 até 500.
sdi = 0
adi = 0
for c in range(1,500+1,2):
    if c % 3 == 0:
        # sdi = sdi + c
        sdi += c
        # cdi = cdi + 1
        adi += 1
    # print(c, end=" ")# no final fazer nada (end="fazer nada")
print(''' a soma de todos os números ímpares multiplos de 3 é igual a {}.
 o total de ímpares somados foi: {} números.'''.format(sdi,adi))
