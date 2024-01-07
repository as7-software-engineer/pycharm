'''
pg que mostar a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. o pg vai ser encerrado quando for digitado valor negativo.
'''
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1,10+1,1):
        print(f'{n} x {c:>2} = {n*c:>7}')
    print('-' * 30)
print('encerrado')