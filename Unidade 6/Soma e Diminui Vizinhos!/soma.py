# coding: utf-8
# Soma e Diminui Vizinhos!
# Iann Carvalho, 2016 / Programação1

def soma_diminui_vizinhos(lista):
	acumulador=0
	for i in range(len(lista)):
		if i % 2 != 0 or i==0:
			acumulador += lista[i]
		else:
			acumulador -= lista[i]
	return acumulador

lista = [1, 2, 3]
assert soma_diminui_vizinhos(lista) == 0
