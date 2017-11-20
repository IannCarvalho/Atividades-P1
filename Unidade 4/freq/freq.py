# coding: utf-8
# Frequência de um elemento em uma sequência
# Iann Carvalho, 2016 / Programação1

#Entrada
num1=raw_input()
sequencia=raw_input()
contador=0
vazio=""
l=[]

for indice in range(len(sequencia)):
	if sequencia[indice]==" ":
		l.append(vazio)
		vazio=""
	else:
		vazio = vazio + sequencia[indice]
l.append(vazio)

for indice in range(len(l)):
	if l[indice]==num1:
		contador=contador+1
	else:
		continue

print contador
