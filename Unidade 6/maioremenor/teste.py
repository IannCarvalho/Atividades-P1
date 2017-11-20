# coding: utf-8
# Retorna Maior e Menor Número
# Iann Carvalho, 2016 / Programação1

def retorna_maior_menor(lista):
	maior=lista[0]
	menor=lista[0]
	l=[]
	for numero in lista:
		if numero>maior:
			maior=numero
		if numero<menor:
			menor=numero
	l.append(maior)
	l.append(menor)
	return l

