# coding: utf-8
# Iann Carvalho / Prog1
# Agrupa Matrículas - Unidade 10

def agrupa_por_periodo(turma):
	novo = {}
	concatenador = ""

	for i in range(len(turma)):
		for y in range(0,3):
			concatenador += turma[i][y]
		if concatenador not in novo.keys():
			novo[concatenador] = 1
		else:
			novo[concatenador] += 1
		concatenador = ""
		
	return novo
