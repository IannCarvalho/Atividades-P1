# coding: utf-8
# Iann Carvalho / Prog1
# Soma Linha e Coluna - Unidade 9

def soma_linha_e_coluna(matriz,l,c):
	acumulador = 0
	for i in range(len(matriz)): #linha
		for y in range(len(matriz[0])): #coluna
			if i == l or y == c:
				if i == l and y == c:
					continue 
				else:		
					acumulador += matriz[i][y]

	return acumulador
