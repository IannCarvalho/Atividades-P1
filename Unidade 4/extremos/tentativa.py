# coding: utf-8
# Classifica Números pelo Menor dos Extremos
# Iann Carvalho, 2016 / Prog1

## QUANTIDADE DE NÚMEROS
num=int(raw_input())

## COLOCANDO TUDO EM UMA LISTA
l=[]
for i in range(num):
	numero=int(raw_input())
	l.append(numero)

## DESCOBRINDO QUAL É O MENOR DOS EXTREMOS
if l[0]>l[-1]:
	menor=l[-1]
else:
	menor=l[0]
print "Menor dos extremos: %d" % (menor)

## DESCOBRINDO MAIORES E MENORES DO QUE O MENOR DOS EXTREMOS
numero_de_menores=0
numero_de_maiores=0
for i in range(len(l)):
	if l[i]>menor:
		numero_de_maiores += 1
	elif l[i]<menor:
		numero_de_menores += 1
	else:
		continue
print "%d número(s) abaixo do menor" % numero_de_menores
print "%d número(s) acima do menor" % numero_de_maiores
