# coding: utf-8
# Iann Carvalho / Prog1
# Matriz Menor - Unidade 9

def matriz_menor(M1, M2):
	z = -1
	nova = []
	for i in range(len(M1)):
		z += 1
		nova.append([])
		for y in range(len(M1[0])):
			if M1[i][y] > M2[i][y]:
				nova[z].append(M2[i][y])
			else:
				nova[z].append(M1[i][y])
	
	return nova		

M1 = [[1,2,3],
      [13,14,15],
      [7,8,9]]

M2= [[10,11,12],
     [4,5,6],
     [7,8,9]]

M3= [[1,2,3],
     [0,0,0],
     [7,8,9]]

assert matriz_menor(M1, M2) == [[1,2,3],[4,5,6],[7,8,9]]
assert matriz_menor(M1, M3) == [[1,2,3],[0,0,0],[7,8,9]]
