# pq q recebe 3 números e mostra o maior e menor.
n1 = float(input(" digite o 1st valor: "))
n2 = float(input(" digite o 2nd valor: "))
n3 = float(input(" digite o 3rd valor: "))
if n1>n2 and n2>n3:
    print(" {} foi o maior valor digitado. E {} foi no menor. ".format(n1,n3))
else:
    if n1>n3 and n3>n2:
        print(" {} foi o maior valor digitado. E {} foi no menor. ".format(n1,n2))
    else:
        if n2>n1 and n1>n3:
            print(" {} foi o maior valor digitado. E {} foi no menor. ".format(n2,n3))
        else:
            if n2>n3 and n3>n1:
                print(" {} foi o maior valor digitado. E {} foi no menor. ".format(n2, n1))
            else:
                if n3>n1 and n1>n2:
                    print(" {} foi o maior valor digitado. E {} foi no menor. ".format(n3, n2))
                else:
                    print(" {} foi o maior valor digitado. E {} foi no menor. ".format(n3, n1))