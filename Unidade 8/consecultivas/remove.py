# coding: utf-8
# Remove Palavras com Letras Iguais Consecutivas
# Iann Carvalho, 2016 / Programação1

def remove_consecutivas(lista):
	consecutivas = False
	for i in range(len(lista)-1, -1, -1):
		palavra = lista[i].lower()
		for y in range(len(palavra)-1):
			if palavra[y] == palavra[y+1]:
				consecutivas = True
				break
		if consecutivas == True:
			consecutivas = False
			lista.pop(i)
			
lista1 = ['arara', 'tv',   'bacia']
assert remove_consecutivas(lista1) == None
assert lista1 == ['arara', 'tv',  'bacia']

lista1 = ['arara', 'arroba',   'bacia']
assert remove_consecutivas(lista1) == None
assert lista1 == ['arara', 'bacia']
	
		
