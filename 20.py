def mes_extenso(mes):
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    try:
        return meses[mes-1]
    except:
        print("Digite um mês válido")
dia = int(input('Digite o Dia: '))
mes = 13
while mes > 12:
    mes = int(input('Digite o Mes: '))
    mes_extenso(mes)
ano = int(input('Digite o Ano: '))
print('%.2i de %s de %i'% (dia,mes_extenso(mes),ano))