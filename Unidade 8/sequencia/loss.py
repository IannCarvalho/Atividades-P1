# coding: utf-8
# Iann Carvalho / Prog1
# Subsequencia 1, 2, 3 - Unidade 8

def tem123plus(l):
	for i in range(len(l)):
		if l[i] == 1:
			guarda_indice = i
			break

	tem_2 = False
	tem_3 = False
	for y in range(i+1, len(l)):
		if tem_2 == True and tem_3 == True:
			break
		elif tem_2 == True:
			if l[y] == 3:
				tem_3 = True
		elif l[y] == 2:
			tem_2 = True

	if tem_2 == True and tem_3 == True:
		return guarda_indice
	else:
		return -1
		
assert tem123plus([3,2,1,2,3]) == 2
assert tem123plus([4,1,1,1,4,2,3]) == 1
assert tem123plus([1,2,2,3]) == 0
assert tem123plus([1,2,2,4]) == -1
