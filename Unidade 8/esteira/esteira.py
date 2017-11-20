# coding: utf-8
# Iann Carvalho / Prog1
# Esteira em uma Linha de Produção de uma Fábrica - Unidade 8

def verifica_esteira(l1,l2):
	contador = 0
	y = 0
	for i in range(len(l1)):
		if y == len(l2):
			break
		elif l1[i] == l2[y]:
			contador += 1
			y += 1

	if y == len(l2):
		return True
	else:
		return False

l1 = [2,1,3,4]
l2 = [2]
assert verifica_esteira(l1,l2)
assert l1 == [2,1,3,4]
assert l2 == [2]

l1 = [1,3,4]
l2 = [4,1]
assert not verifica_esteira(l1,l2)
assert l1 == [1,3,4]
