# coding: utf-8
# Iann Carvalho / Prog1
# Unidade de medida - Unidade 

unidades = {'km':1000,'hm':100,'dam':10,'m':1,'dm':0.1,'cm':0.01,'mm':0.001}

while True:
	medida = raw_input().split()
	parte1 = (float(medida[0]) * unidades[medida[1]])
	parte2 = (float(medida[2]) * unidades[medida[3]])
	if parte1 == 0 and parte2 == 0:
		break
	print "%.2f m" %(parte1 + parte2)

