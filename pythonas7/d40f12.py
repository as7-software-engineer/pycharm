# leia duas notas de um aluno
# mostrando seu média e mensagem no final dizendo reprovado <5 recuperação 5 a 6.9 aprovado 7 pra cima
cores = {"limpa":"\033[m","azul":"\033[34m","amarelo":"\033[33m","pretoebranco":"\033[7:30m","verde":"\033[32m","vermelho":"\033[31m","negritoac":"\033[1;35m"}
nota1 = float(input(" primeira nota: "))
nota2 = float(input(" primeira nota: "))
media = (nota1 + nota2) / 2
print(" tirando {} e {} a média do aluno é {}{:.1f} ".format(nota1, nota2, cores["verde"], media))
if 7 > media >=5:
    print("o aluno está em \033[33mRECUPERAÇÃO\033[m. ")
elif 5 > media:
    print(" o aluno está \033[31mREPROVADO\033[m. ")
else:
    print(" o aluno está \033[32mAPROVADO\033[m. ")