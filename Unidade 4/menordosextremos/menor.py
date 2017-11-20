# coding: utf-8
# Menor Palavra dos Extremos
# Iann Carvalho / prog1 2016

#entrada
quantidade=int(raw_input())

#listas e laços de entrada
lmenores=[]
l=[]
lmaiores=[]
for i in range(quantidade):
	nome=raw_input()
	l.append(nome)

#conversão de valores
primeira_palavra= l[0]
ultima_palavra= l[-1]
letras_primeira= len(l[0])
letras_ultima= len(l[-1])

#condicional
if letras_primeira<letras_ultima:
	for y in range(1,quantidade):
		if len(l[y])<letras_primeira:
			lmenores.append(l[y])
		elif letras_primeira<len(l[y]):
			lmaiores.append(l[y])
		else:
			continue
	lista_maiores=len(lmaiores)
	lista_menores=len(lmenores)
	print """Menor palavra dos extremos: %s (%d letras)
%d palavra(s) com tamanho menor
%d palavra(s) com tamanho maior""" % (primeira_palavra, letras_primeira , lista_menores, lista_maiores)
elif letras_ultima<letras_primeira:
	for y in range(0, quantidade-1):
		if len(l[y])<letras_ultima:
			lmenores.append(l[y])
		elif letras_ultima<len(l[y]):
			lmaiores.append(l[y])
		else:
			continue
	lista_maiores=len(lmaiores)
	lista_menores=len(lmenores)
	print """Menor palavra dos extremos: %s (%d letras)
%d palavra(s) com tamanho menor
%d palavra(s) com tamanho maior""" % (ultima_palavra, letras_ultima , lista_menores, lista_maiores)
else:
	for y in range(1, quantidade-1):
		if len(l[y])<letras_ultima:
			lmenores.append(l[y])
		elif letras_ultima<len(l[y]):
			lmaiores.append(l[y])
		else:
			continue
	lista_maiores=len(lmaiores)
	lista_menores=len(lmenores)
	print """Menor palavra dos extremos: %s, %s (%d letras)
%d palavra(s) com tamanho menor
%d palavra(s) com tamanho maior""" % (primeira_palavra, ultima_palavra, letras_ultima, lista_menores, lista_maiores)
