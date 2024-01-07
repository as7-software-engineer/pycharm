'''faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. caso contrário peça a digitação novamente até ter um valor correto.
famosa validação de dados'''
sexo = str(input("informe seu sexo: [M/F]")).strip().upper()[0] #remover os espaços, botar pra maisculo e pegar a primeira letra.
while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(' Sexo {} registrado com sucesso'.format(sexo))
