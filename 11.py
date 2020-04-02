inter = [200.0, 299.0, 300.0, 399.0, 400.0, 499.0, 500.0, 599.0, 600.0, 699.0, 700.0, 799.0, 800.0, 899.0, 900.0, 999.0, 1000.0, 'ou mais']
lista_vendedores = []
valor_brutos = 0
menu = 1;
count = 0
count2 = 0
while menu != '0':
    valor_brutos = float(input('Digite o valor total de sua vendas brutas na semana: '));
    salario = float(200 + valor_brutos*9/100);
    print(salario)
    lista_vendedores.append(salario)
    menu = input('Cadastrar mais um vendedor (1)\nVerificar quantos vendedores receberam salários em certos intervalos (0)\n\t\t>>');
lista_vendedores.sort()
menu = 1;
print('\t\tIntervalos!')
for i in range(1,len(inter)+1):
    if i % 2 == 0:
        count2 += 1
        print(inter[count], f'({count2})')
    else:
        print(inter[count], '', end="")
    count += 1
while menu != '0':
    count = 0
    count_vender = 0
    verificar = int(input('\nDigite o intervalo: '))
    for i in lista_vendedores:
        if verificar != 9:
            if i >= inter[(verificar-1)*2] and i <= inter[(verificar-1)*2+1]:
                count_vender += 1;
        elif i >= inter[(verificar-1)*2]:
            count_vender += 1;
    print(f'{count_vender} vendedores recebem esse salário!')
    menu = input('Verificar outro intervalo (1)\nSair (0)\n\t\t>>');