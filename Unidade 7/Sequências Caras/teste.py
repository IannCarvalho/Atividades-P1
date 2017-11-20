# coding: utf-8
# Maiores e Menores
# Iann Carvalho, 2016 / Programação1

def sequencia_caras(lancamentos):
	l=[]
	contador=0
	for i in range(len(lancamentos)):
		if lancamentos[i]==1:
			contador += 1
		else:
			l.append(contador)
			contador=0
	l.append(contador)
	maior=0
	for numero in l:
		if numero>maior:
			maior=numero
	return maior
		

			
			
