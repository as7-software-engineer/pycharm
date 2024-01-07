'''pg com função leiaInt(), que vai funcionar de forma semlhante á função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
ex:
n = leiaInt('Digite um n')
'''
# n = int(input("Digite um número: "))
# print(f'Você acabou de digitar o número {n}')
cores = {"limpa":"\033[m","azul":"\033[34m","amarelo":"\033[33m","pretoebranco":"\033[7:30m","verde":"\033[32m","vermelho":"\033[31m","negritoac":"\033[1;35m"}



def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'{cores["vermelho"]}ERRO! Digite um número inteiro válido!{cores["limpa"]}')
        if ok:
            break
    return valor
n = leiaInt("Digite um número: ")
print(f'{cores["verde"]}Você acabou de digitar o número {n}{cores["limpa"]}')
