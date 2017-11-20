# coding: utf-8
# Altera Consecutivos (Inverte 2 a 2)
# Iann Carvalho, 2016 / Programação1

def inverte2a2_condicional(seq):
	for i in range(0, len(seq)-1, 2):
		if seq [i] > seq [i+1]:
			seq[i], seq[i+1] = seq[i+1], seq[i]
	return seq
