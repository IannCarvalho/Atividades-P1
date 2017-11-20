# coding: utf-8
# Iann Carvalho / Prog1
# Zera Diagonal - Unidade 9

def zera_diagonal(m):
	for y in range(len(m[0])): # COLUNA
		for i in range(len(m)): # LINHA
			if i == y:
				m[i][y] = 0

m = [[8, 20, -7],
     [ 5, 1,  3],
     [ 6,  7, 9]]

zera_diagonal(m)
assert  m == [[0, 20, -7], [5, 0, 3], [6, 7, 0]]
