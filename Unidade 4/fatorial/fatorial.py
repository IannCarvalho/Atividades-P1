# coding: utf-8
# Fatorial
# Iann Carvalho, 2016 / Prog1

numero=int(raw_input())
acumulador=1

for i in range(numero, 0, -1):
	acumulador = acumulador * i
	
print acumulador
