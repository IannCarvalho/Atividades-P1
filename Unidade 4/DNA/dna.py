# coding: utf-8
# Sequencia de DNA
# Iann Carvalho, 2016 / Programação1

#Entrada
ent1=raw_input()
ent2=raw_input()

#Condicional
numero_de_letras=len(ent1)
contador=0
for indice in range(0, len(ent1), 1):
	if ent1[indice] == ent2[indice]:
		contador = contador + 1

metade_letras=len(ent1)/2

if contador > metade_letras:
	print 'sim'
else:
	print 'nao'
