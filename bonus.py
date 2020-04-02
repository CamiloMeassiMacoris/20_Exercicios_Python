def numero_extenso(num):
	"""
	Função que retorna o numero por extenso
	Entrada valida: 0 - 1 000 000
	Para entradas maiores que um milhão retorna: número invalido!
	"""
	
	zero_desenove = {0:"", 1:"um", 2:"dois", 3:"três", 4:"quatro", 5:"cinco", 6:"seis", 7:"sete", 8:"oito", 9:"nove", 10:"dez", 11:"onze", 12:"doze", 13:"treze", 14:"quatorze", 15:"quize", 16:"dezesseis", 17:"dezessete", 18:"dezoito", 19:"dezenove"}
	dezenas = {0: '', 2:"vinte", 3:"trinta", 4:"quarenta", 5:"cinquenta", 6:"sessenta", 7:"setenta", 8:"oitenta", 9:"noventa"}
	centenas = {0: '', 1:"cento", 2:"duzentos", 3:"trezentos", 4:"quatrocentos", 5:"quinhentos", 6:"seiscentos", 7:"setecentos", 8:"oitocentos", 9:"novecentos"}
	saida = []
	lista = [centenas,dezenas,zero_desenove]
	if int(num) > 1000000 or int(num) < 0:
		return "número inválido!"
	else:
		numero = num
		numero = numero.zfill(7)
		
		uni = int(numero[-1])
		dez = int(numero[-2])
		cen = int(numero[-3])
		mil = int(numero[-4])
		mil_dez = int(numero[-5])
		mil_cen = int(numero[-6])
		milhao = int(numero[-7])
		lista_casa = [cen,dez,uni]
		lista_casaMil = [mil_cen,mil_dez,mil]
		lista_master = [lista_casa,lista_casaMil]
		cont = 0
		if milhao != 0:
			return 'um Milhão'
		if mil == 0 and mil_dez == 0 and mil_cen == 0:
			for i in lista_casa:
				if i == 0:
					cont += 1
				if cont == 3:
					return 'zero'
				if cen == 1 and cont == 2:
					return 'cem'
		for n in range(1,-1,-1):
			if mil == 0 and mil_dez == 0 and mil_cen == 0:
				mil = 1
				continue
			for i in range(3):
				if i == 1 and lista_master[n][1] == 1:
					saida.append(lista[i+1][int(str(lista_master[n][1])+str(lista_master[n][2]))])
					break
				else:
					saida.append(lista[i][lista_master[n][i]])
					if i == 2:
						break
			if (mil != 0 or mil_dez != 0 or mil_cen != 0) and n == 1:
				saida.append(' mil')
		while True:
			cont = 0
			for i in range(len(saida)):
				if saida[i] == '':
					del(saida[i])
					break
				cont += 1
			if cont == len(saida):
				break
		for i in range(len(saida)-1,0,-1):
			if saida[i-1] != ' e ' and saida[i] != ' mil':
				saida.insert(i,' e ')
		for i in range(len(saida)):
			if saida[i] == 'cento' and saida[i+1] == ' mil':
				saida[i] = 'cem'
		return ''.join(saida)

n = input("Digite um numero de zero a um milhão: ")
print(numero_extenso(n))