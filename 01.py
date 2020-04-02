import os
h = 'a'
while True:
    os.system('cls')
    try:
        h = float(input('Digite sua altura: '))
        break
    except:
        print('Digite um número!')
        continue
    
validacao = ['h','H','m','M']
while True:
    sexo = input('Digite "H" se for homem e "M" se for mulher ')    
    cont = 0
    for i in validacao:
        cont+=1
        if sexo != i and cont == 4:
            print('Digite "H" para homem ou "M" para mulher')
            cont+=1
            break
        elif sexo == i:
            break
    if cont == 5:
        continue
    elif cont >=3:
        print('Seu peso ideal é %.2f'% ((62.1*h)-44.7))
        break
    else:
        print('Seu peso ideal é %.2f'% ((72.7*h)-58))
        break
            