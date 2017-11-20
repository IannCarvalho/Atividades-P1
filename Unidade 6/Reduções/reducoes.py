# coding: utf-8
# Reduções
# Iann Carvalho, 2016 / Programação1

def reducoes(seq):
	l=[]
	for i in range(len(seq)-1):
		sub = seq[i] - seq[i+1]
		if sub<0:
			sub=0
		l.append(sub)
	return l
	
