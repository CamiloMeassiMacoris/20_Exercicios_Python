lados = []
for i in range(3):
    lados.append(float(input('Digite o lado {0}: '.format(i+1))))
if (lados[0] + lados[1]) > lados[2] and  (lados[0] + lados[2]) > lados[1] and (lados[1] + lados[2]) > lados[0]:
    print('É um Triângulo')
    if lados[0] == lados[1] and lados[0] == lados[2]:
        print('É um Triângulo Equilátero')
    elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
        print('É um Triângulo Isósceles')
    elif lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
        print('É um Triângulo Escaleno')
else:
    print('Não é um Triângulo')