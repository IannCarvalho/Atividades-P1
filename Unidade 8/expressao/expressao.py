# coding: utf-8
# Expressão Regular Simples
# Iann Carvalho, 2016 / Programação1

def is_substring_expr(str1,str2):
	lstr1=[]
	lstr2 = str2.split('*')

	y = 0
	conta = 0
	repetido = 0

	for i in range(len(str1)):
		while y<(len(lstr2[0])):
			if str1[i] == lstr2[0][y]:
				conta += 1
				y += 1
				break
			else:
				conta = 0
				break

	if conta == len(lstr2[0]):
		repetido += 1
	
	conta = 0
	y = len(lstr2[1])-1
	
	for i in range(len(str1)-1, -1, -1):
		while y>-1:
			if str1[i] == lstr2[1][y]:
				conta += 1
				y -= 1
				break
			else:
				conta = 0
				break

	if conta == len(lstr2[1]):
		repetido += 1
	
	if repetido == 2:
		return True
	else:
		return False
