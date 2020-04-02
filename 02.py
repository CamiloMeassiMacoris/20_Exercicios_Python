peso = float(input('Digite quantos Kg foi pescado: '));
if(peso>50):
    excesso = peso - 50;
    multa = excesso * 4;
    print('Peso: {0}\nExcesso: {1:.2f}\nMulta: {2:.2f}'.format(peso,excesso,multa))
else:
    print('Peso: ', peso)
