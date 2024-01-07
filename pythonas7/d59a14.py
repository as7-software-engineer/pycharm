'''crie um pg que leia 2 valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
seu programa deverá realizar a operação solicitada em cada caso.'''
n1 = int(input('Primeiro valor: '))
n2 = int(input("segundo valor: "))
o = 0
while o != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sai do pg''')
    o = int(input('qual é sua opção? '))
    if o == 1:
        soma = n1+n2
        print('A soma entre {} e {} é {}'.format(soma))
    elif o == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}. '.format(n1,n2,produto))
    elif o == 3:
        if n1 > n2:
           print(" {} é maior que {}.".format(n1,n2))
        elif n1 < n2:
           print(" {} é maior que {}.".format(n2,n1))
        else:
           print(" os valores são iguais.".format(n1, n2))
    elif o == 4:
        print('Informe outros dois números!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input("segundo valor: "))
    elif o == 5:
        print('finalizando')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*16)
print('Fim do programa! Volte sempre!')