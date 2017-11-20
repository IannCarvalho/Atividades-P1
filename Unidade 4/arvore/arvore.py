# coding: utf-8
# Desenhando uma Árvore de Natal
# Iann Carvalho, 2016 / Programação1

#entrada
num=int(raw_input())

for indice in range(0, num, 1):
	base_arvore= ((num-indice-1) * " ") + "o" * (2*indice) + "o"
	
	print base_arvore
	
print (num-1)*" " + "o"





#num tem que diminuir a cada laço
