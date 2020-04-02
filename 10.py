num = []
maior = 0
maior_sete = 0
while True:
    num.append(float(input('Entre com um valor: ')))
    if num[len(num)-1] == -1.0:
        del(num[len(num)-1])
        break
print('\nTamanho:',len(num))
print('\nValores na ordem em que foram informados:',num)
num.reverse()
print('\nValores na ordem inversa à que foram informados:', num)
print('\nSoma dos valores:', sum(num))
media = sum(num)/len(num)
print('\nMédia dos valores:', media)
for i in num:
    if i > media:
        maior += 1
print('\nQuantidade de valores acima da média:', maior)
for i in num:
    if i < 7:
        maior_sete += 1
print('\nQuantidade de valores abaixo de sete:', maior_sete)
print('\nTchau!!')