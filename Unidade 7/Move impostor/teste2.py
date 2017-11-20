# coding: utf-8
# Move Impostor
# Iann Carvalho, 2016 / Programação1

def move_impostor(lista):
	for i in range(len(lista)-1):
		if lista[i] > lista[i+1]:
			impostor=lista[i+1]
			break
	for y in range(i, -1,-1):
		if lista[y]>lista[y+1]:
			lista[y], lista[y+1] = lista[y+1], lista[y]
