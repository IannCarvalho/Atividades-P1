# coding: utf-8
# Subtração de Polinomios
# Iann Carvalho, 2016 / Programação1

def subtrai_polinomios(p1, p2):
	if len(p1)>len(p2):
		while len(p1) != len(p2):
			p2.append(0)
	else: 
		while len(p1) != len(p2):
			p1.append(0)

	p3=[]	
	for i in range(len(p1)):
		p3.append((p1[i]-p2[i]))
	
	while p3[-1] == 0:
		p3.pop(-1)
		
	return p3
	
p1 = [-5, 4, 3]
p2 = [-1, 0, 2, 0, 0, 0, 5]
assert subtrai_polinomios(p1, p2) == [-4, 4, 1, 0, 0, 0, -5]

p1 = [-5, 4, 3]  # 3x2 + 4x - 5
p2 = [-4, 2, 3]  # 3x2 + 2x - 4
assert subtrai_polinomios(p1, p2) == [-1, 2]  # 2x - 1
