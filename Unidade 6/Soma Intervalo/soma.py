# coding: utf-8
# Soma Intervalo
# Iann Carvalho, 2016 / Programação1

def soma_intervalo(a,b):
	acumulador=0
	for i in range(a, b+1, 1):
		acumulador += i
	print acumulador
	return acumulador

assert soma_intervalo(5,15) == 110
assert soma_intervalo(10,10) == 10
