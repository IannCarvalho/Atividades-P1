# coding: utf-8
# Letras Dobradas
# Iann Carvalho, 2016 / Prog1

num=int(raw_input())
dobradas=[]
ndobradas=[]
contador=0

for i in range(num):
	palavra_da_vez=raw_input()
	for i in range(len(palavra_da_vez)-1):
		segunda_letra = palavra_da_vez[i + 1]
		primeira_letra = palavra_da_vez[i]
		penultima_letra = palavra_da_vez[-2]
		if primeira_letra == segunda_letra:
			dobradas.append(palavra_da_vez)
			contador=contador+1
			break
		else:
			continue
	if contador==0:
		ndobradas.append(palavra_da_vez)
	contador=0
			

print "%d palavra(s) com letras dobradas:" % (len(dobradas))

for i in range(len(dobradas)):
	print dobradas[i]
	
print "---"
print "%d palavra(s) sem letras dobradas:" % (len(ndobradas))

for i in range(len(ndobradas)):
	print ndobradas[i]
