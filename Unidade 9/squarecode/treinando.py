# coding: utf-8
# Iann Carvalho / Prog1
# Square Code - Unidade 9

def square_code(string):
	import math
	lista_string = []
	for k in range(len(string)-1,-1,-1):
		if string[k].isalpha():
			lista_string.append(string[k])
	lista_string = lista_string[::-1]
	linhas = int(math.floor(len(lista_string)**(0.5)))
	colunas = int(math.ceil(len(lista_string)/float(linhas)))
	matriz = []
	w = 0
	for i in range(linhas):
		matriz.append([])
		t = 0
		while t < colunas:
			if w < len(lista_string):
				matriz[i].append(lista_string[w])
				w += 1
			else:
				matriz[i].append("")
			t += 1
	resultante = ''
	for k in range(colunas):
		for j in range(linhas):
			resultante += matriz[j][k]
		if k != colunas-1:
			resultante += " "
	return resultante
	

