usuarios = []
espaco = []
count = 0
menu = 1
while menu != 0:
    while True:
        usuarios.insert(count, input('Nome do usuário (máx: 15 characters): '))
        if len(usuarios[count]) > 15:
            print('Digite um nome com no máximo 15 characters')
        else:
            tam = len(usuarios[count])
            usuarios[count] = usuarios[count] + ' '*(15-tam)
            break
    espaco.append(float(input('Espaço usado por ele em MB: ')))
    count += 1
    menu = int(input('Deseja cadastrar mais 1 usuário (1)\nTerminou de Cadastrar (0)\n\t\t>>'))

total_espaço = sum(espaco)
print('\nNr.\tusuario\t\tEspaço utlizado\t\t\t% do uso')
for i in range(len(usuarios)):
    porce_uso = round(espaco[i]*100/total_espaço, 2)
    print(f'\n{i+1}\t{usuarios[i]}\t\t{espaco[i]}MB\t\t\t{porce_uso}%')
print(f'Espaço total ocupado: {total_espaço}\nEspaço médio ocupado: {total_espaço/len(espaco)}')