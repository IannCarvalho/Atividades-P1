# coding: utf-8
# Iann Carvalho / Prog1
# Busca por Coluna - Unidade 9

def busca_todos_por_coluna_em_matriz(m, e):
	lugares=[]
	for y in range(len(m[0])): # COLUNA
		for i in range(len(m)): # LINHA
			if m[i][y] == e:
				lugares.append((i,y))
	
	return lugares
	
matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [3, 2, 3, 2, 1],
]
assert busca_todos_por_coluna_em_matriz(matriz, 4) == []
assert busca_todos_por_coluna_em_matriz(matriz, 3) == [(1,0), (2,0), (0,1), (2,2), (0,3)]
assert busca_todos_por_coluna_em_matriz(matriz, 1) == [(1,2), (0,4), (2,4)]
