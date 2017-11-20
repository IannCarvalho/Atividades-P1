# coding: utf-8
# Criação de uma Nova Palavra
# Iann Carvalho, 2016 / Prog1

palavra=raw_input()
numero=(raw_input())

acumulador=""

for i in range (len(palavra)):
	numero_da_vez = int(numero[-i - 1]) + 1
	letra = palavra[i] * numero_da_vez
	acumulador = acumulador + letra
	
print acumulador
