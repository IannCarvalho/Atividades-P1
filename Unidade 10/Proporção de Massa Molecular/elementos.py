# coding: utf-8
# Iann Carvalho / Prog1
# Elementos Químicos - Unidade 10

def elementosQuimicos(lista):
	soma = 0
	elementos_massa = {'H':1,'S':32,'O':16,'C':12,'Ca':40,'Na':23,'P':31} # tabela das moleculas
	for i in range(len(lista)):
		if lista[i].isdigit(): # verifica se a string pode ser um digito ou não
			digito = int(lista[i])
			soma += digito*elementos_massa[lista[i-1]] - elementos_massa[lista[i-1]] # caso seja um digito retiro o valor anterior e multiplico

		else:
			
			soma += elementos_massa[lista[i]]
	return soma

entrada = raw_input().split()
while entrada[0] != 'fim':
	print elementosQuimicos(entrada)
	entrada = raw_input().split()
