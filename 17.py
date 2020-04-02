def valorPagamento(valor,dias):
    if dias == 0:
        return valor
    elif dias > 0:
        return valor + valor*3/100 + valor*0.1/100*10
    else:
        return valor
prestacoes = []
sair = 1
while sair != 0:
    valor = float(input('Digite o valor da prestação: '))
    atraso = int(input('Digite os dias de atraso: '))
    prestacoes.append(valorPagamento(valor,atraso))
    sair = int(input('Adicionar outra prestação (1)\nEncerrar (0)\n>>'))

print(f'Quantidade de prestações: {len(prestacoes)}\nTotal do valor: {sum(prestacoes)}')