# coding: utf-8
# Conversão de Matrículas na UFCG
# Iann Carvalho, 2016 / Programação1

#entrada
antigo = raw_input()

#utilitários
list(antigo)
vazio = ""
contador = 0
lista = []
antigo = list(antigo)
zero = "0"

#Mudando primeiro número
antigo[0]="1"

#quebrando em duas partes
for indice in range(len(antigo)):
	if contador == 5:
		lista.append(vazio)
		contador = 0
		vazio = antigo[indice]
	else:
		vazio = vazio + antigo[indice]
		contador = contador + 1
lista.append(vazio)

#somando o zero no meio das partes
resultado = lista[0] + zero + lista[1]
print resultado
