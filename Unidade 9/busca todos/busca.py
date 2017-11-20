# coding: utf-8
# Iann Carvalho / Prog1
# Busca Todos em Matriz - Unidade 9

def busca_matriz(m, e):
	lugares=[]
	for i in range(len(m)): # LINHA
		for y in range(len(m[i])): # COLUNA
			if m[i][y] == e:
				lugares.append((i,y))
	
	return lugares

matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [1, 2, 3, 2, 1],
]
assert busca_matriz(matriz, 4) == []
assert set(busca_matriz(matriz, 3)) == set( [(0,1), (0,3), (1,0), (2,2)] )
