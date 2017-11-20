# coding: utf-8
# Iann Carvalho/ prog1
# União de Listas

def uniao_listas(l1,l2):
	for i in range(len(l2)):
		if not verificaRepetidos(l1,l2[i]):
			l1.append(l2[i])
	removeRepetidos(l1)



def verificaRepetidos(l1,elementoespecifico):
	for i in range(len(l1)):
		if l1[i] == elementoespecifico:
			return True
	return False

def removeRepetidos(l1):
	for i in range(len(l1)-1,0,-1):
		if l1[i] == l1[i-1]:
			l1.pop(i)

l1 = [2,1,3,4]
l2 = [2]
assert uniao_listas(l1,l2) == None
assert l1 == [2,1,3,4]
assert l2 == [2]

l1 = [1,3,4]
l2 = [4]
assert uniao_listas(l1,l2) == None
assert l1 == [1,3,4]
assert l2 == [4]

l1 = [2,4,1]
l2 = [6,7,91]
uniao_listas(l1,l2)
assert l1 == [2,4,1,6,7,91]
assert l2 == [6,7,91]

l2 = [6,7,91,2, 4, 12, 14, 1]
l1 = []
assert uniao_listas(l1,l2) == None
assert l1 == [6,7,91,2, 4, 12, 14, 1]
