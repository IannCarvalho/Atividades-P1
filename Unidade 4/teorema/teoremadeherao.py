# coding: utf-8
# Utilizando o Teorema de Herão para Calcular a Área de Triângulos
# Iann Carvalho, 2016 / Programação1

import math
# Entrada
num=int(raw_input())

l=[]
lareas=[]
for i in range(num):
	a=str(raw_input())
	vazio = ''
	for i in range(len(a)):
		if a[i]==' ':
			l.append(vazio)
			vazio=''
		else:
			vazio=vazio+a[i]
	l.append(vazio)
	vazio=''
	a=float(l[0])
	b=float(l[1])
	c=float(l[2])
	s= (a+b+c) / 2
	A = math.sqrt ( s * (s-a) * (s-b) * (s-c) )
	l=[]
	lareas.append(A)

media_areas=0
lareas_100=[]
for i in range(len(lareas)):
	print "Área %d: %.2f" %((i+1), lareas[i])
	if lareas[i]>100:
		lareas_100.append(lareas[i])

if len(lareas_100)>0:
	acumulador=0
	for i in range(len(lareas_100)):
		acumulador=acumulador+lareas_100[i]
	area_media = ( (acumulador) / len(lareas_100) )
	print "Número maiores: %d, área média: %.2f" %(len(lareas_100), area_media)
	
	
