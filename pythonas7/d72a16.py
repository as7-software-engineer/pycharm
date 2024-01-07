# pg que tenha tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# seu pg deverá ler um n pelo teclado entre 0 e 20) e mostrá-lo por extenso.
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0<= núm <= 20:
        break
    print('tente novamente. ', end='')
print(f'Vc digitou o número {cont[núm]}')