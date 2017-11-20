# coding: utf-8
# Seleciona Divisores em uma Lista
# Iann Carvalho, 2016 / Programação1

def filtra_divisores(lista):
	for i in range(len(lista)-1, -1, -1):
		string = str(lista[i])
		acumulador = 0
		for y in range(len(string)):
			acumulador += int(string[y])
		if lista[i] % acumulador != 0:
			lista.pop(i)
			
lista1 = [333, 121, 81]
assert filtra_divisores(lista1) == None
assert lista1 == [333,81]
