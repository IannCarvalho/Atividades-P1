# coding: utf-8
# Iann Carvalho / Prog1
# Inverte Dicionário - Unidade 10

def inverte_dicionario(dic):
	novo = {}
	valores = dic.values()
	chaves = dic.keys()
	l=[]
	auxiliar = []
		
	for i in range(len(valores)):
		if valores[i] not in auxiliar:
			l.append(chaves[i])
			for y in range(i+1, len(valores)):
				if valores[i] == valores[y]:
					l.append(chaves[i])
		novo[valores[i]]=l
			
	return novo
