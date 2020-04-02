#Não entendi o porque dos "3%" dos sindicatos
hora = float(input('Digite o valor de sua hora: '))
qnd_hora = int(input('Digite a quantidade de horas trabalhada no mês: '))
salario = float(hora*qnd_hora)
if(hora*qnd_hora)<900:
    ir = 0
elif (hora*qnd_hora)<1500:
    ir = 5
elif(hora*qnd_hora)<2500:
    ir = 10
else:
    ir = 20
ir_de = float((salario * ir)/100)
inss = float((salario * 10)/100)
salario_liquido = float(salario-(ir_de+inss))
print('Salário Bruto: ({0} * {1}) :\t R$ {2}'.format(hora,qnd_hora,salario))
print('(-) IR ({0}%) :\t\t\t R$ {1}'.format(ir,ir_de))
print('(-) INSS (10%) :\t\t R$', inss)
print('FGTS (11%) :\t\t\t R$', (salario * 11)/100)
print('Total de descontos :\t\t R$', salario-salario_liquido)
print('Salário Liquido :\t\t R$', salario_liquido)