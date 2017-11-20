# coding: utf-8
# Quantos Comeram?
# Iann Carvalho, 2016 / Programação1

def quantos_comeram(N, fila):
	acumulador = 0
	for i in range(len(fila)):
		if fila[i] <= N:
			acumulador += fila[i]
			N = N - fila[i]
		else:
			break
	return acumulador
