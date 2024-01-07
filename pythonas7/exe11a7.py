l = float(input('qual o valor da largura? '))
a = float(input('qual o valor da altura? '))
m2 = l*a
pintura = m2/2
tdt = pintura*4
print('a área deste ambiente é de {} metros quadrados. \n sabendo-se que, com 1 litro de tinta, você consegue pintar 2 metros quadrados. \n para pintar todas as paredes você vai precisar de {} litros de tinta. '.format(m2,tdt))