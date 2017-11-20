# coding: utf-8
# Calcula DV
# Iann Carvalho, 2016 / prog1

frase=raw_input()

frase_minuscula=frase.lower()
contador=0
vogais=["a","e", "i", "o", "u"]

for i in range(0, len(frase), 1):
	for indice in range(len(vogais)): 
		if frase_minuscula[i]==vogais[indice]:
			print frase[i]
			contador = contador + 1
	if contador == 1:
		break
	
		
if contador==0:
	print "-"
	
