# coding: utf-8
# Maioridade Penal
# Iann Carvalho, 2016 / Prog1

a=int(raw_input())
b=int(raw_input())
k=int(raw_input())

## PEGANDO OS MULTIPLOS DE A
multiplosa=[]
for i in range(a, k+1, a):
	multiplosa.append(i)
	
## PEGANDO OS MULTIPLOS DE B
multiplosb=[]	
for i in range(b, k+1, b):
	multiplosb.append(i)

## SELECIONANDO OS MULTIPLOS EM COMUM
for i in range(len(multiplosa)):
	for y in range(len(multiplosb)):
		if multiplosb[y]==multiplosa[i]:
			print multiplosa[i]
		
