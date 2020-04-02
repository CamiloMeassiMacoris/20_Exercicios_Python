def somar_TaxaImposto(taxaImposto, valor):
    return valor + valor*taxaImposto/100

arg1 = int(input('Digite a taxa: '))
arg2 = float(input('Digite o valor: '))
print(somar_TaxaImposto(arg1,arg2))