def value(arg):
    if(arg>0):
        return "P"
    elif(arg<1):
        return "N"

num = int(input('Digite um inteiro para verificar se é positivo ou negativo: '))
print('(P) Positivo (N) Negativo\nResultado:',value(num))