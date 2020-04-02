n = 1
m = 1
tam = int(input('Coloque o tamanho: '))
somatorio = []
somatorio2 = []
print("s = ", end = "")
for n in range(1,tam+1):
    print(n, "/", m, " + ", end="")
    somatorio.append(n)
    somatorio2.append(m)
    n += 1
    m += 2
print(" = ", sum(somatorio), "/", sum(somatorio2))