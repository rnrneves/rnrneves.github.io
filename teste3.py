N = int(input("Digite um numero positivo: "))
if 1 < N < 1000:
    for i in range(1, N + 1):
        print(i)
        print(i*2)
else:
    print("Numero invalido. Digite um numero entre 2 999")