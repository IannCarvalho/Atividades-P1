# coding: utf-8
# Letras Alternadas
# Iann Carvalho, 2016 / Programação1

def letras_alternadas(palavra):
	nova=""
	for i in range(len(palavra)):
		if i%2==0:
			nova += palavra[i]
	return nova
		
