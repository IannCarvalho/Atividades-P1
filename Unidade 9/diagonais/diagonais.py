# coding: utf-8
# Iann Carvalho / Prog1
# Diagonais - Unidade 9

def diagonais(m):
	l=[]
	
	esquerda_para_direita = []
	for i in range(len(m)):
		for y in range(len(m[0])):
			if i == y:
				esquerda_para_direita.append(m[i][y])

	direita_para_esquerda = []
	for i in range(len(m)):
		for y in range(-1 ,-len(m[0])-1, -1):
			if i == -(y+1):
				direita_para_esquerda.append(m[i][y])

	l.append(esquerda_para_direita)
	l.append(direita_para_esquerda)

	return l
	
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

assert diagonais(M) == [[1,5,9],[3,5,7]]
