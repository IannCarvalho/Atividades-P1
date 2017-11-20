# coding: utf-8
# Iann Carvalho / Prog1
# Soma Matriz Interna - Unidade 9

def soma_matriz_interna(matriz, inicio, fim):
	acumulador = 0
	for i in range(len(matriz)):  # LINHA
		if i>=inicio[0] and i<=fim[0]:
			for y in range(len(matriz[0])):  # Coluna
				if y>=inicio[1] and y<=fim[1]:
					acumulador += matriz[i][y]

	return acumulador

M2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
assert soma_matriz_interna(M2, (1,1),(2,2)) == 5 + 6 + 8 + 9
