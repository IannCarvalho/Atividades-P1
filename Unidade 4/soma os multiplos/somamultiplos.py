# coding: utf-8
# Soma os Múltiplos do Primeiro Elemento de uma Lista
# Iann Carvalho, 2016 / prog1

entrada=int(raw_input())

acumulador=0

for i in range(0, 10, 1):
	num_da_vez=int(raw_input())
	if num_da_vez % entrada == 0:
		acumulador= acumulador + num_da_vez

print acumulador
