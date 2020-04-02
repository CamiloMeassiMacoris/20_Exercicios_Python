score = []
scor = 0
print('Escreva (n) para não ou (s) para sim')
perguntas = ["Telefonou para a vítima: ","Esteve no local do crime: ","Mora perto da vítima: ","Devia para a vítima: ","Já trabalhou com a vítima: "]
for i in range(5):
    while True: 
        print(perguntas[i], end="")
        score.insert(i,input().upper())
        if score[i] == 'S' or score[i] == 'N':
            if score[i] == 'S':
                scor += 1;
            break
        else:
            print('Escreva (n) para não ou (s) para sim')

if scor < 2:
    print('Você é Inocênte')
elif scor == 2:
    print('Você é Suspeito(a)')
elif scor > 2 and scor < 5:
    print('Você é Cúmplice')
else:
    print('Você é Assasino(a)')