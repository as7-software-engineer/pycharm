# crie um pg que mostre todos os números pares que estão no intervalo entre 1 e 50.
# for n in range(2,50+1,2):
#     print(n, end=' ')
for n in range(1,50+1):
    print(".", end="")
    if n % 2==0:
     print(n, end=' ')
print('acabou')

