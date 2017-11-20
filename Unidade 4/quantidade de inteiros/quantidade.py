# coding: utf-8
# Classificação de Elementos Utilizando a Média dos Extremos
# Iann Carvalho, 2016 / prog1

k=int(raw_input())

sequencia=int(raw_input())

contador=0

for i in range(0, sequencia, 1):
	numero_da_vez = int(raw_input())
	if numero_da_vez % k == 0:
		contador = contador + 1
	else:
		continue
		
porcentagem = (contador*100.0) / sequencia
simbolo = "%"

print "%d (%.1f%s)" % (contador, porcentagem, simbolo)
