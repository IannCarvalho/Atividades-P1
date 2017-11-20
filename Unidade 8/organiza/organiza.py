# coding: utf-8
# Iann Carvalho / Prog1
# Organiza Lista pela Média - Unidade 8

def organiza_por_media(lista):
	if lista==[]:
		return lista
	acumulador = 0
	for i in range(len(lista)):
		acumulador += lista[i]

	media = float(acumulador) / len(lista)

	for i in range(len(lista)-2, -1, -1):
		if lista[i] > media:
			for y in range(i+1, len(lista)):
				if lista[y] <= media:
					lista[y-1], lista[y] = lista[y], lista[y-1]
				else:
					break
					
	return lista
	
p1 = [1,2,4,1,3,4,56,7,7,4,3,67]
assert organiza_por_media(p1) == [1,2,4,1,3,4,7,7,4,3,56,67]
