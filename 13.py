def somar(x, y, z):
    try:
        return float(x)+float(y)+float(z)
    except:
        return x+y+z
print('Somar 3 argumentos (string ou float)')
n = []
for i in range(3):
    n.append(input(f'Digite o argumento {i+1}: '))
print('Resultado:', somar(n[0],n[1],n[2]))