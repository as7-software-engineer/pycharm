'''crie um pg que vai gerar cinco números aleatórios e colocar em uma tupla.
depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
# from random import randint
# números = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)) # de um até 10 gerando um valor aleatório.
# print(f'Eu sorteei os valores {números}')  # mostra (x,x,x,x,x)

from random import randint
números = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)) # de um até 10 gerando um valor aleatório.
print(' Os valores sorteados foram :')
for n in números:
    print(f' {n} ', end='') #mostra x x x x x
'''vamos usar o método max() que funciona em tuplas tbm'''
print(f"\n O maior valor sorteado foi {max(números)}")
print(f" O menor valor sorteado foi {min(números)}")
