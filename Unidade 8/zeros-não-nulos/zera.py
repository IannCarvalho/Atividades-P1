# coding: utf-8
# Iann Carvalho / Prog1
# Zera não-nulos! - Unidade 9

def zera_nao_nulos(m, lin, col):
	# ACHANDO PONTO DE INTERCESSÃO
	if m[lin][col] != 0:
		m[lin][col] = 0

	# MUDANDO A PARTE DE CIMA	
	for cima in range(lin-1, -1, -1):
		if m[cima][col] != 0:
			m[cima][col] = 0
		else:
			break

	# MUDANDO A PARTE DE BAIXO
	for baixo in range(lin+1, len(m)):
		if m[baixo][col] != 0:
			m[baixo][col] = 0
		else:
			break

	# MUDANDO A PARTE DA DIREITA
	for direita in range(col+1,len(m[0])):
		if m[lin][direita] != 0:
			m[lin][direita] = 0
		else:
			break

	# MUDANDO A PARTE DA ESQUERDA
	for esquerda in range(col-1, -1, -1):
		if m[lin][esquerda] != 0:
			m[lin][esquerda] = 0
		else:
			break
			
jogo = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]    

zera_nao_nulos(jogo, 3, 2)

assert jogo == [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
] 
