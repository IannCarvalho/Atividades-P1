# coding: utf-8
# Remove Menores de uma Lista
# Iann Carvalho, 2016 / Programação1

def remove_menores(N, lista):
	contador=0
	for i in range(len(lista)-1, -1, -1):
		if lista[i] < N:
			contador += 1
			lista.pop(i)
	return contador

lista = [1, 2, 3, 4, 5]
assert remove_menores(3, lista) == 2
assert lista == [3, 4, 5]
