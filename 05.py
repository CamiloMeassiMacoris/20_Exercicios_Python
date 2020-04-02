litros = float(input('Digite a quantidade de litros vendidos: '))
tipo = ['a','A','g','G']
while True:
    combustivel = input('Digite o tipo do combustivel "G" para gasolina ou "A" para álcool: ')  
    cont = 0
    for i in tipo:
        cont+=1
        if combustivel != i and cont == 4:
            print('Digite "G" para gasolina ou "A" para álcool')
            cont+=1
            break
        elif combustivel == i:
            break
    if cont == 5:
        continue
    elif cont >=3:
        print('O valor a ser pago será de R$', litros*2.5)
        break
    else:
        print('O valor a ser pago será de R$', litros*1.9)
        break