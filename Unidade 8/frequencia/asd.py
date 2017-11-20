# coding: utf-8
# Iann Carvalho / Prog1
# Frequencia - Unidade 8

def meu_in(elemento, l2):
	repetido = False
	for i in range(len(l2)):
		if l2[i] == elemento:
			repetido = True
			break
	return repetido

def get_frequencia(l):
	l2=[]
	resposta=[]
	for i in range(len(l)):
		contador = 1
		if not meu_in(l[i], l2):
			l2.append(l[i])
			for y in range(i+1,len(l)):
				if l[y] == l[i]:
					contador += 1
			resposta.append(contador)
	return resposta
	
assert get_frequencia(['b','b','c','b', 'a']) == [3,1,1]
