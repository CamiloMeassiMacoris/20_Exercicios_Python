import os
gabarito = ['A','B','C','D','E','E','D','C','B','A'];
nota_todos = [[]for i in range(40)];
nota=[];
pontos_aluno = [];
cont = 0;
while True:
    os.system('cls')
    pontos = 0;
    for i in range(len(gabarito)):
        nota_todos[cont].append(input(f'Digite a resposta da {i+1}: ').upper())
        if nota_todos[cont][i] == gabarito[i]:
            pontos += 1;
    pontos_aluno.append(pontos);
    while True:
        try:
            menu = int(input('Outro aluno vai usar o sistema (1)\nTodos alunos já utilizaram (0)\n\t\t\t>>'))
            if(menu>1):
                print('Digite (1) ou (0)')
            else:
                break
        except:
            print('Digite (1) ou (0)')
    if menu == 0:
        break
    cont += 1;
os.system('cls')
pontos_aluno.sort()
print(f'Maior Acerto: {pontos_aluno[len(pontos_aluno)-1]}\nMenor Acerto: {pontos_aluno[0]}\nTotal de Alunos que utilizaram o sistemas: {len(pontos_aluno)}\nMédia de notas dos Alunos {sum(pontos_aluno)/len(pontos_aluno)}')
