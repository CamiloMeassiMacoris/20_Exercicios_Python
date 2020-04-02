def horario_ap(horas):
    if horas > 12 and horas != 24:
        return [(horas-12),'P.M']
    elif horas == 24:
        return [12,'A.M']
    elif horas == 12:
        return [12,'P.M']
    else:
        return [horas,'A.M']
def horario_24h(horas,tipo):
    if tipo == 'A':
        if horas == 12:
            return 0
        else:
            return horas
    else:
        if horas == 12:
            return 12
        else:
            return (horas + 12)

while True:
    print('Converter horario do formato 24h para o formato A.M P.M (1)')
    print('Converter horario do formato A.M P.M para o formato 24h (2)')
    print('Sair (0)')
    menu = int(input('>>'))
    if menu == 1:
        horas = int(input('Digite as horas em formato 24h: '))
        minutos = int(input('Digite os minutos: '))
        print('%.2i:%.2i %s'%(horario_ap(horas)[0],minutos,horario_ap(horas)[1]))
    elif menu == 2:
        horas = int(input('Digite as horas em formato A.M/P.M: '))
        minutos = int(input('Digite os minutos: '))
        tipo = input('Digite o tipo "A" para A.M ou "P" para P.M: ').upper()
        print('%.2i:%.2i'%(horario_24h(horas,tipo),minutos))
    elif menu == 0:
        break
