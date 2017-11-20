# coding: utf-8
# Get Itens
# Iann Carvalho, 2016 / Programação1

def get_items(valores, indices):
	l=[]
	for indice in indices:
		if indice>len(valores)-1:
			l.append(None)
		else:
			l.append(valores[indice])
	return l

valores = [18, 22, 73, 32, 19, 21, 43]
indices = [3, 4, 8, 1]
assert get_items(valores, indices) == [32, 19, None, 22]

	
	
	
