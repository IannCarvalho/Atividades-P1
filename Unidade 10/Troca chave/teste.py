# coding: utf-8
# Iann Carvalho / Prog1
# Troca Chave - Unidade 10

def troca_chave(dic):
	novo = {}
	chaves = dic.keys()
	valores = dic.values()

	for i in range(len(dic)):
		novo[valores[i]]=chaves[i]

	return novo

assert troca_chave({1:2}) == {2:1}
assert troca_chave({1:2, 2:3, 3:4}) == {2:1, 3:2, 4:3}
assert troca_chave({ '@':'V','a':'v', 'n':'o'}) == { 'V':'@','v':'a', 'o':'n'}
