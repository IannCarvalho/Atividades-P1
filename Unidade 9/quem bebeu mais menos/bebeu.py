# coding: utf-8
# Iann Carvalho / Prog1
# Quem bebeu mais menos - Unidade 9

def quem_bebeu_mais_menos(m, m2):
	l1=[]
	acumulador = 0
	for i in range(len(m[0])):
		for y in range(len(m)):
			acumulador += m[y][i]
		l1.append(acumulador)
		acumulador = 0
	
	l2=[]
	acumulador = 0
	for i in range(len(m2[0])):
		for y in range(len(m2)):
			acumulador += m2[y][i]
		l2.append(acumulador)
		acumulador = 0

	l3=[]
	for i in range(len(m2)):
		da_vez= l1[i] + l2[i]
		l3.append(da_vez)
	
	indice_maior = 1
	indice_menor = 1
	menor = l3[0]
	maior = l3[0]
	indice_maior = 1
	indice_menor = 1
	for i in range(len(l3)):
		if menor > l3[i]:
			indice_menor = i + 1
			menor = l3[i]
		if maior < l3[i]:
			indice_maior = i + 1
			maior = l3[i]

	return (indice_maior, indice_menor)	

sabado = [[1,2,3],
		  [0,1,0],
		  [3,1,2]]
domingo = [[2,1,3],
		   [0,2,1],
		   [1,1,2]]
assert quem_bebeu_mais_menos(sabado, domingo) == (3,1)

sabado = [[1,2,3,4,5],
		  [0,1,2,3,1],
		  [2,1,0,1,2],
		  [3,1,2,1,3],
		  [4,1,3,0,0]]
domingo = [[0,1,1,0,1],
		   [1,2,2,0,2],
		   [2,3,1,1,1],
		   [3,4,2,0,0],
		   [4,3,3,0,0]]
assert quem_bebeu_mais_menos(sabado, domingo) == (1,4)
