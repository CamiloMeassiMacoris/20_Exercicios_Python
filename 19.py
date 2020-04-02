def num(num):
    b = []
    b.extend(num)
    b.reverse()
    return b

number = input('Digite um valor para ser imprimido ele invertido: ')
print('Valor invertido: ', end="")
print(''.join(num(number)))