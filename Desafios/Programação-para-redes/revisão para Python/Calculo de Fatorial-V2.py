def fat(n):
    if n==0:
        return 1
    else:
        return n*fat(n-1)
n = int(input("Qual o Fatorial de:"))
print (fat(n))